from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario

from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
    return render_template('login.html')

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario: 
        return redirect(url_for('auth.signup'))

    new_user = Usuario(email=email, name=name, password=generate_password_hash(password, method='sha256'))      

    db.session(new_user)
    db.session()

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'
