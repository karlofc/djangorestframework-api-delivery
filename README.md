# djangorestframework-api-delivery

## Set virtual environment
- python -m venv env
- env/Scripts/activate.bat

## Install dependencies
- pip install django (Django installation)
- pip install python-decouple (Separe settings from code)
- pip install djangorestframework
- pip install django-phonenumber-field[phonenumbers]

### Dependencies list for pip
- pip freeze > requirements.txt

## Create project
- django-admin startproject delivery .

## Test Server
- python manage.py runserver

## Create application
- python manage.py startapp authentication
- python manage.py startapp orders

## Available sub-commands list
- python manage.py

## Generate HEX token
- python
- inport secrets
- secrets.token_hex(12)

## Generate models file creation
- python manage.py makemigrations authentication

## Reply models to db tables
- python manage.py migrate (in case of error delete db.sqlite3)

## Crate Super User
- python manage.py createsuperuser