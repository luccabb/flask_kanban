# Welcome to CS162 Final Project

## Run Virtual Environment

Virtual environment is a key component in ensuring that the application is configured in the right environment

##### Requirements
* Python 3
* Pip 3

```bash
$ brew install python3
```

Pip3 is installed with Python3

##### Installation
To install virtualenv via pip run:
```bash
$ pip3 install virtualenv
```

##### Usage
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

All environment variables are stored within the `.env` file and loaded with dotenv package.

**Never** commit your local settings to the Github repository!

## Run Application

Start the server by running:

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

## Deployment

The website is deployed on heroku and can be accessed on the following url: https://kanban-app-cs162.herokuapp.com/
