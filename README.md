# URL Shortener

A simple URL shortener built with Flask and MariaDB.

## Features

    Shorten long URLs into shorter ones
    Redirect to original URL when visiting the shortened URL

## How to use

    Run the application by executing python app.py
    Send a post method to http://localhost:5000/shorten-url with the url parameter
    The shortened URL will be displayed

## Database Configuration

The application uses a MariaDB database to store the shortened URLs. The database configuration is stored in a .env file.

## Environment Variables

    DB_USER: the database username
    DB_PASSWORD: the database password
    DB_NAME: the database name
    DB_ROOT_PASSWORD: the root password for the database
