# manageflow [![Build Status](https://travis-ci.com/jitingcn/manageflow.svg?branch=master)](https://travis-ci.com/jitingcn/manageflow)

manageflow is a task manager app for a group of users with multiple roles. (WIP)

The building version are:

* Python 3.6+
* Django 3

## Setting Up for Development

These are instructions for setting up this project
in development environment, may vary depending on your operating system.

* install Python on your system, you can also use [conda](https://docs.conda.io/en/latest/) or [pyenv](https://github.com/pyenv/pyenv):

    You’ll need to make sure you have python and pip available. You can check this by running:

        $ python --version
        Python 3.7.6
        $ pip --version
        pip 20.0.2

* install [pipenv](https://github.com/pypa/pipenv):

        $ pip install pipenv

* check out project code:

        $ git clone https://github.com/jitingcn/manageflow
        $ cd manageflow

* prepare pipenv environment and install requirements

        $ pipenv shell
        (manageflow) $ pipenv install --dev

* manageflow is configured to use a SQLite database by default. To use
  PostgreSQL or MySQL database, create and edit `manageflow/local_settings.py` file.
  There is a template you can copy and edit as needed:

        (manageflow) $ cp manageflow/local_settings.py.example manageflow/local_settings.py

* create database tables and the superuser account:

        (manageflow) $ ./manage.py migrate
        (manageflow) $ ./manage.py createsuperuser

* run development server:

        $ ./manage.py runserver

* deploy script for linux:

        $ ./deploy.sh
