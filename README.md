# CS162 Kanban Board

The website is deployed on heroku and can be accessed on the following url: https://kanban-app-cs162.herokuapp.com/

## Project Structure

`/web` contains application code.

`/web/static` css files.

`/web/templates` html files.

`/web/__init__.py` project initializer file.

`/web/auth.py` routes related to authorization/authentication.

`/web/config.py` different configurations based on running environment (test/dev/prod).

`/web/models.py` ORM mapping (from DB models to python classes) using SQLAlchemy.

`/web/routes.py` application routes.

`/unit_test` contains 25 unit tests in total. Tests for: registration, login, reset password, and kanban operations (todo, doing, done).

`/migrations` directory used to control DB migrations, using Flask-migrate.

`.env/example` contains all variables needed on your .env so the project runs on production or locally.

`Procfile` used for heroku deployment.

## Virtual Environment
Creation of virtualenv:

    $ virtualenv -p python3 venv

If the above code does not work, you could also do

    $ python3 -m venv venv

To activate the virtualenv:

    $ source venv/bin/activate

Or, if you are **using Windows** - [reference source:](https://stackoverflow.com/questions/8921188/issue-with-virtualenv-cannot-activate)

    $ venv\Scripts\activate

To deactivate the virtualenv (after you finished working):

    $ deactivate

Install dependencies in virtual environment:

    $ pip3 install -r requirements.txt

## Environment Variables

`.env.example` is a file containing all the environment variables that you need to define in a `.env` file for this project to run.

## Run Application

Start the server on a mac locally by running:

    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ export FLASK_ENV=dev
    $ export FLASK_APP=web
    $ python3 -m flask run

## Unit Tests
To run the unit tests on mac use the following commands:

    $ source venv/bin/activate
    $ pip install -r requirements.txt
    $ export FLASK_ENV=test
    $ export SECRET_KEY='test-key'
    $ pytest unit_test
