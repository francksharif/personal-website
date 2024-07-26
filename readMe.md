# Personal Site

A personal website built with Flask, PostgreSQL, and TailwindCSS to showcase my projects. The site includes an admin dashboard for managing projects.

## Table of Contents
- [Introduction](#introduction)
- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)

## Introduction
This project aims to create a personal website to publish my projects and allow others to view them. It includes an admin dashboard accessible only by the admin to manage projects (create, read, update, delete).

## Installation
### Prerequisites
- Python 3.x
- Flask
- PostgreSQL (or other database you like)
- Node.js (for TailwindCSS)

### Steps
1. Clone the repository:
   ```sh
   git clone https://github.com/your-username/personal-site.git
   cd personal-site

2. Create virtual environment and activate it:
    ```sh
   python3 -m venv venv
   source venv/bin/activate

3. Install the python dependencies:
    ```sh
    pip install -r requirements.txt

4. Install Node.js dependencies for TailwindCSS:
    ```sh
    npm install

## Configuration
1. Create en `.env` file in the root directory with the following content:
    ```env
    FLASK_APP=run.py
    FLASK_ENV=development
    DATABASE_URL=postgresql://user:password@localhost/dbname
    SECRET_KEY=your_secret_key

2. Configure the database by modifying the `config.py`

## Usage
### Running the Development Server
    flask run

### Compiling TailwindCSS
#### In a separate terminal, run:
    npx tailwindcss -i ./src/input.css -o ./dist/output.css --watch

### Features
- Admin Dashboard: Manage projects with CRUD operations.
- Authentication: Secure login for the admin.

