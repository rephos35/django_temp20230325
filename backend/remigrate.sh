#! /bin/bash

# rm mysqldb
# not to rm migrations 
# pipenv run python manage.py makemigrations account
# pipenv run python manage.py migrate --fake account zero
# pipenv run python manage.py migrate --fake-initial account zero


pipenv run python manage.py migrate --fake 
pipenv run python manage.py migrate --fake-initial 

pipenv run python manage.py makemigrations account
pipenv run python manage.py migrate