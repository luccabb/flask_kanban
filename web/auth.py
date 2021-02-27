from flask import Flask, render_template, request, redirect, url_for, Blueprint, flash
from .models import db, User
import json
from flask_login import LoginManager, logout_user, current_user, login_user
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, Form, BooleanField, validators
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo, Length
from passlib.hash import pbkdf2_sha256

class LoginForm(FlaskForm):
    email = StringField('Email')
    password = PasswordField('Password')

class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired(), Length(min=4, max=25)])
    email = StringField('Email Address', validators=[Email(), Length(min=6, max=35)])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField('Repeat Password', validators=[DataRequired(), EqualTo('password')])

    # def validate_username(self, username):
    #     user = User.query.filter_by(username=username.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different username.')

    # def validate_email(self, email):
    #     user = User.query.filter_by(email=email.data).first()
    #     if user is not None:
    #         raise ValidationError('Please use a different email address.')

login_manager = LoginManager()
# new application blueprint for routes
auth = Blueprint('auth', __name__, template_folder='templates')

@login_manager.user_loader
def load_user(id):
    return User.query.get(int(id))

@auth.route('/signup', methods=['GET', 'POST'])
def signup():
    if request.method == 'GET':
        form = RegistrationForm(request.form)
        if current_user and current_user.is_authenticated:
            return redirect(url_for('routes.index'))
        return render_template('signup.html', form=form)
    
    elif request.method == 'POST':
        form = RegistrationForm(request.form)
        if not form.validate_on_submit():
            print("Signup form errors:", form.errors.items())
        
        if form.validate_on_submit():
            user = User(username=form.username.data, email=form.email.data, password=pbkdf2_sha256.hash(form.password.data))
            db.session.add(user)
            db.session.commit()
            return redirect(url_for('auth.login'))

def check_password(user_password, password):
    return pbkdf2_sha256.verify(password, user_password)

@auth.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm(request.form)
    if request.method == 'GET':
        if current_user and current_user.is_authenticated:
            return redirect(url_for('routes.index'))
        return render_template('login.html', form=form)
    else:
        if not form.validate_on_submit():
            print("Login form errors:", form.errors.items())

        if form.validate_on_submit():
            # Login and validate the user.
            # user should be an instance of your `User` class
            user = User.query.filter_by(email=form.email.data).first()
            if user is None or not check_password(user.password, form.password.data):
                flash('Invalid username or password')
                return redirect(url_for('auth.login'))
            login_user(user)

            return redirect(url_for('routes.index'))

@auth.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('routes.index'))
