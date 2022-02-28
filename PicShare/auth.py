from flask import Blueprint, flash, render_template, request
from werkzeug.security import generate_password_hash, check_password_hash
from .checkPasswordStrength import passwordStrength
from .validateEmail import validEmail

from .modules import session

auth = Blueprint(
    'auth',
    __name__,
    url_prefix='/'
)

# AIM: to deal with user logins and registeration

@auth.route('/login', methods=['POST', 'GET'])
def usr_login():
    if request.method == 'POST':
        pass
    return render_template('login.html')

@auth.route('/registeration', methods=['POST', 'GET'])
def usr_registeration():
    if request.method == 'POST':
        newUser_details = request.form
        username = newUser_details.get('username')
        usr_email = newUser_details.get('email')
        password = newUser_details.get('password')
        password2 = newUser_details.get('re-confirm')

        # email and password validators
        password1 = passwordStrength(password)
        email = validEmail(usr_email)
        
    return render_template('register.html')