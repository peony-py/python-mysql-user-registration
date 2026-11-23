
### a personal learning project developed to practice Python,MySQL, input validation, and secure password hashing

# Python MySQL User Registration

A command-line user registration application built with Python and MySQL.

## Features

Email validation
Password validation
Secure password hashing using Argon2
User registration in MySQL
Prevention of duplicate usernames
Database error handling
Environment-based database configuration

## Technologies

Python
MySQL
mysql-connector-python
email-validator
argon2-cffi
python-dotenv

## Project Structure

`login_form.py` - Main application
`schema.sql` - Database structure
`requirements.txt` - Required packages
`.env.example` - Example configuration
`.gitignore` - Excluded files

## Installation

1. Clone the repository.
2. Create a Python virtual environment.
3. Install dependencies:

    pip install -r requirements.txt

4. Create a `.env` file based on `.env.example`.
5. Configure your MySQL credentials.
6. Execute `schema.sql` in MySQL Workbench.
7. Run the application:

    python login_form.py

## Security

- Passwords are hashed using Argon2.
- Database credentials are stored in environment variables.
- SQL queries use parameterized statements.

## Project Purpose

This project was developed to practice Python backend fundamentals, MySQL integration, input validation, and secure password storage.
