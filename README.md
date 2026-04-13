# Django Models

[Link to Latest PR](https://github.com/ticochuck/djangocustom-user/pull/1)

## Description

Create an app user Custom User. 
Make the email address the username. Username must be unique. 


## Usage

- `poetry shell` to start your virtual environment
- `poetry install` to install dependencies
- create .env file with the following variables and save it into 'snacks_project' directory
    - SECRET_KEY=secret key for the app (typically 50-characters long string)
    - DEBUG=should be set to True in development
    - ALLOWED_HOSTS=localhost,127.0.0.1 (for testing)
- `python manage.py makemigrations` - to generate DB schema
- `python manage.py migrate` - to create DB schema
- `python manage.py createsuperuser` - to create user with admin access
- `python manage.py collectstatic` - to collect apps static files
- `python manage.py runserver` - to run server

## Tests
- Verify the creation of a new user with email and password
- Verify that duplicate emails are not allowed

## Lab26 - Django Custom User

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160047)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)


## References
[Custom User Email]https://learndjango.com/tutorials/django-log-in-email-not-username)
[Exceptions](https://docs.djangoproject.com/en/3.1/ref/exceptions/)