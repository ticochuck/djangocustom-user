# Django Custom User

[Link to Latest PR](https://github.com/ticochuck/django_custom_user/pull/1)

## Description

- Create Django application from scratch that has a custom user model named CustomUser
- Custom user should use email instead of username for signup / login
- Application should work with Django Admin


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
Use Django’s built in testing tools
- Verify the creation of a new user with email and password
- Verify that duplicate emails are not allowed

## Lab29 - Django Custom User

[Canvas Assignment](https://canvas.instructure.com/courses/2045906/assignments/15160047)

## Author

[Chuck Li Villalobos](https://github.com/ticochuck)


## References
[Email Auth](https://learndjango.com/tutorials/django-log-in-email-not-username)
