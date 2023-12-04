from flask import Flask, render_template, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_login import LoginManager, UserMixin, login_user, login_required, logout_user, current_user
from flask import request, redirect, url_for, flash, g
from flask_migrate import Migrate
from flask import current_app
from werkzeug.security import generate_password_hash, check_password_hash
import re


app = Flask(__name__)
app.secret_key = 'moodsculpt123'
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moodsculpt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)
login_manager = LoginManager(app)
login_manager.login_view = 'login'


class User(db.Model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    last_connected = db.Column(db.DateTime)


@app.after_request
def add_header(response):
    response.headers['Cache-Control'] = 'no-store, no-cache, must-revalidate, post-check=0, pre-check=0, max-age=0'
    response.headers['Pragma'] = 'no-cache'
    response.headers['Expires'] = '-1'
    return response


@app.before_request
def before_request():
    if request.endpoint and request.endpoint in ['login', 'signup'] and current_user.is_authenticated:
        return redirect(url_for('index'))


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


@app.route('/')
def index():
    response = make_response(render_template('index.html'))
    response.headers['Cache-Control'] = 'public, max-age=300'
    return response


@app.route('/mood', methods=['POST'])
@login_required
def add_mood():
    mood = request.form.get('mood')
    flash(f'You feel {mood} today!')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        identifier = request.form.get('identifier', '')
        password = request.form.get('password', '')

        print(f"Login Attempt - Identifier: {identifier}")
        print(f"Password: {password}")
        user = User.query.filter(db.or_(User.username == identifier, User.email == identifier)).first()
        if user and check_password_hash(user.password, password):
            login_user(user)
            return redirect(url_for('index'))
        else:
            flash('Invalid Email or password', 'error')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        confirm_password = request.form.get('confirm-password')
        email = request.form.get('email')
        existing_email = User.query.filter_by(email=email).first()
        existing_user = User.query.filter_by(username=username).first()
        if not re.match(r"[^@]+@[^@]+\.[^@]+", email):
            flash('Invalid Email format', 'error')
        elif existing_email:
            flash('Email is already taken', 'error')
        elif existing_user:
            flash('Username is already taken', 'error')
        elif password != confirm_password:
            flash('Passwords do not match', 'error')
        elif len(password) < 8:
            flash('Password must be Strong', 'error')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password, email=email)
            db.session.add(new_user)
            db.session.commit()
            login_user(new_user)
            return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout')
@login_required
def logout():
    username = current_user.username
    logout_user()
    return redirect(url_for('login'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
    app.run(debug=True)