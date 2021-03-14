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

## Run Application

Start the server on a mac locally by running:

    $ source env/bin/activate
    $ pip install -r requirements-unit.txt
    $ export FLASK_ENV=dev
    $ export FLASK_APP=web
    $ python3 -m flask run

## Unit Tests
To run the unit tests on mac use the following commands:

    $ source env/bin/activate
    $ pip install -r requirements-unit.txt
    $ export FLASK_ENV=test
    $ export SECRET_KEY='test-key'
    $ pytest unit_test
