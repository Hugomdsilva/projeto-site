from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
from . import db

auth = Blueprint('auth', __name__)

@auth.route('/login')
def login():
    return render_template('login_page/login.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #codigo pra validar e adicionar usuarios para base de dados
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

    user = User.query.filter_by(email=email).firts

    if user:
        return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))

@auth.route('/logout')
def logout():
    return 'Logout'