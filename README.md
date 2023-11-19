# MoodSculpt

MoodSculpt is a web application designed to help users track their moods, gain insights into their emotional well-being, and improve mental health through personalized analytics and rewards.

## Table of Contents

- [Features](#features)
- [Architecture](#architecture)
- [API Documentation](#api-documentation)
- [Data Model](#data-model)
- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [Authors](#authors)
- [License](#license)

## Features

- Log and track daily moods
- View personalized insights and patterns
- User-friendly interface for seamless mood entry

## Architecture

MoodSculpt is built using:

- Front-end: HTML, CSS, JavaScript
- Back-end: Flask, MySQL
- API: RESTful API principles
- Database: MySQL
- Version Control: Git
- Deployment: Yet to be decided

## API Documentation

### API Routes for Web Client to Web Server Communication

- `/api/moods`:

  - GET: Retrieve all mood entries for the logged-in user.
  - POST: Add a new mood entry for the logged-in user.

- `/api/insights`:

  - GET: Retrieve insights into the logged-in user's mood patterns.

- `/api/auth`:

  - POST: Authenticate the user and log them in.

- `/api/register`:
  - POST: Register a new user.

### API Endpoints or Function/Methods for Other Clients to Use

No API endpoints provided for other clients in MoodSculpt.

### Data Model

Refer to the [Data Model Diagram](link-to-diagram) for details on entities and relationships.

## Installation

1. Clone the repository: `git clone https://github.com/ChahirSaid/MoodSculpt.git`
2. Navigate to the project directory: `cd MoodSculpt`
3. Install dependencies: `pip install -r requirements.txt`
4. Set up the database: `python manage.py migrate`

## Usage

1. Run the development server: `python manage.py runserver`
2. Access the application at [http://localhost:8000](http://localhost:8000)

## Contributing

We welcome contributions! If you have suggestions, bug reports, or want to contribute code, please follow our [Contribution Guidelines](CONTRIBUTING.md).

## Authors

To view the list of contributors, check the [AUTHORS](AUTHORS) file in the project root.

## License

This project is licensed under the [MIT License](LICENSE).
