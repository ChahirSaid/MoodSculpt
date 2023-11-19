# MoodSculpt - Mood Journal Project

## Table of Contents

- [Overview](#overview)
- [Features](#features)
- [Getting Started](#getting-started)
  - [Prerequisites](#prerequisites)
  - [Installation](#installation)
  - [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)
- [Authors](#authors)
- [Acknowledgments](#acknowledgments)

## Overview

MoodSculpt is a web-based mood journal application that allows users to track and manage their emotions over time. The project is built using Flask, HTML, CSS, and SQLite for database storage.

## Features

- **User Authentication:**
  - Sign up and log in securely to access personalized mood tracking.

- **Mood Tracking:**
  - Record and visualize your daily moods.
  - Add notes and tags to provide context to your mood entries.

- **Responsive Design:**
  - Enjoy a seamless experience on various devices, including desktops, tablets, and smartphones.

## Getting Started

### Prerequisites

- [Python](https://www.python.org/) installed on your machine
- [Flask](https://flask.palletsprojects.com/en/2.1.x/) framework

### Installation

1. Clone the repository:
   git clone https://github.com/ChahirSaid/MoodSculpt.git
Change into the project directory:
   cd MoodSculpt

Install dependencies:
   pip install -r requirements.txt

Set up the database:
   flask db init
   flask db migrate
   flask db upgrade
   
Run the application:
   python app.py
   
Visit http://localhost:5000 in your web browser.

### Usage
Sign Up:
   Create an account with a unique username and password.
Log In:
   Log in to access your personalized mood tracking dashboard.
Record Mood:
   Add daily mood entries, including notes and tags.
Visualize Your Mood:
   View your mood history and trends.
   
## Contributing
If you'd like to contribute to MoodSculpt, please follow these steps:
   Fork the repository.
   Create a new branch (git checkout -b feature/your-feature-name).
   Make your changes and commit them (git commit -am 'Add some feature').
   Push to the branch (git push origin feature/your-feature-name).
   Create a new Pull Request.

## Authors
Said Chahir - [Github](https://github.com/ChahirSaid)  
Othmane Boubecheur - [Github](https://github.com/glackyy) / [Twitter](https://twitter.com/glackybeatz)

## License
This project is licensed under the MIT License.

## Acknowledgments
Thank you to the contributors who have helped make this project possible.
Feel free to customize the sections based on the specifics of your project. Include any additional information or details that would be relevant to users or potential contributors.
