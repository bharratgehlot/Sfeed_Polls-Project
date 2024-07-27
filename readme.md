# Sfeed or Student Feedback Polls Project

## Overview
This project is a web application developed using Django, a high-level Python web framework. It utilizes PostgreSQL as its database management system.

## Features
- Created using Django, a Python web framework.
- Uses PostgreSQL for database storage.

## Setup Instructions
To run this project locally, follow these steps:
- pip install -r requirements.txt
- database setup

  DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'your_database_name',
        'USER': 'your_database_user',
        'PASSWORD': 'your_database_password',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}

- python manage.py migrate
- python manage.py runserver

## Contact
Repository URL - https://github.com/bharratgehlot/Sfeed_Polls-Project

## Features to be added

 - One should able to fill survey many times but his/her vote should not be included after one try
 - Design set of 25 questions about collegue infrasturcture
 - Design set of 20 question about placement
 - Design set of 20 questions for alumanies.
 - Design set of 20 questions for financal related stuff
 - Change to more appealing layout

##I have stopped working on this to focus on other projects  
