#!/usr/bin/env bash

DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"

cd "$DIR" || exit 1
pipenv install || pip install -r requirements.txt || exit 2
pipenv run python manage.py makemigrations
pipenv run python manage.py migrate
pipenv run python manage.py compilemessages
pipenv run python manage.py compress --force
pipenv run python manage.py collectstatic --no-input
pipenv run python population_script.py || exit 3
