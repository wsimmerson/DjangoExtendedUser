Drop in Django app with an extendable User model which used E-Mail as the username by default

Do this before running your first migrations

Usage:
  drop users folder into your django project
  add 'users' to installed apps in settings.py
  set AUTH_USER_MODEL = 'users.ExtendedUser' in settings.py
  manage.py makemigrations users
  manage.py migrate