from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask import request, redirect, url_for
from flask import session, flash
from werkzeug.security import generate_password_hash, check_password_hash


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///moodsculpt.db'
app.config['SQLALCHEMY_TRACK_MODIFICATION'] = False
db = SQLAlchemy(app)


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(50), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)


@app.route('/')
def index():
    return render_template('index.html')


@app.route('/mood', methods=['POST'])
def add_mood():
    if 'username' not in session:
        return redirect(url_for('login'))
    mood = request.form.get('mood')
    flash(f'You feel {mood} today!')
    return redirect(url_for('index'))


@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        user = User.query.filter_by(username=username).first()

        if user and check_password_hash(user.password, password):
            session['username'] = username
            flash(f'Welcome back, {username}!')
            return redirect(url_for('index'))
        else:
            flash('Invalid username or password')

    return render_template('login.html')


@app.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')

        existing_user = User.query.filter_by(username=username).first()
        if existing_user:
            flash('Username is already taken. Please choose another.')
        else:
            hashed_password = generate_password_hash(password)
            new_user = User(username=username, password=hashed_password)
            db.session.add(new_user)
            db.session.commit()
            flash('Account created successfully. Please login.')
            return redirect(url_for('login'))

    return render_template('signup.html')


@app.route('/logout')
def logout():
    session.pop('username', None)
    flash('You have been logged out.')
    return redirect(url_for('index'))


if __name__ == '__main__':
    with app.app_context():
        db.create_all()
        app.run(debug=True)
