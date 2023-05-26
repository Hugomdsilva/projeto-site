<<<<<<< HEAD
<<<<<<< Updated upstream
from flask import Blueprint, render_template, redirect, url_for, request, flash
from werkzeug.security import generate_password_hash, check_password_hash
from .models import Usuario

from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User

=======
from flask import Blueprint, render_template
>>>>>>> Stashed changes
=======
from flask import Blueprint, render_template, redirect, url_for, request
from werkzeug.security import generate_password_hash, check_password_hash
from .models import User
>>>>>>> 5ca24cbbffc959e596b3557007c6cdeb34580a1e
from . import db

auth = Blueprint('auth', __name__)


@auth.route('/login')
def login():
<<<<<<< HEAD
<<<<<<< Updated upstream

    return render_template('login.html')
=======
    return render_template('login_page/login.html')
>>>>>>> Stashed changes

@auth.route('/signup')
def signup():
    return render_template('signup.html')

@auth.route('/signup', methods=['POST'])
def signup_post():

    return render_template('login_page/login.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #codigo pra validar e adicionar usuarios para base de dados

=======
    return render_template('login_page/login.html')

@auth.route('/signup', methods=['POST'])
def signup_post():
    #codigo pra validar e adicionar usuarios para base de dados
>>>>>>> 5ca24cbbffc959e596b3557007c6cdeb34580a1e
    email = request.form.get('email')
    name = request.form.get('name')
    password = request.form.get('password')

<<<<<<< HEAD

    usuario = Usuario.query.filter_by(email=email).first()

    if usuario: 
        return redirect(url_for('auth.signup'))

    new_user = Usuario(email=email, name=name, password=generate_password_hash(password, method='sha256'))

    db.session.add(new_user)
    db.session.commit()

    return redirect(url_for('auth.login'))

=======
>>>>>>> 5ca24cbbffc959e596b3557007c6cdeb34580a1e
    user = User.query.filter_by(email=email).firts

    if user:
        return redirect(url_for('auth.signup'))

    return redirect(url_for('auth.login'))
<<<<<<< HEAD

=======
>>>>>>> 5ca24cbbffc959e596b3557007c6cdeb34580a1e

@auth.route('/logout')
def logout():
    return 'Logout'
