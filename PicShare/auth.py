from flask import Blueprint, flash, redirect, render_template, request, url_for
from werkzeug.security import generate_password_hash, check_password_hash
from .checkPasswordStrength import passwordStrength
from .validateEmail import validEmail
from .models import Users
from . import db

auth = Blueprint(
    'auth',
    __name__,
    url_prefix='/'
)

# AIM: to deal with user logins and registeration

@auth.route('/login', methods=['POST', 'GET'])
def usr_login():
    if request.method == 'POST':
        email = request.form.get('email').lower()
        password = request.form.get('password')

        usr_email = validEmail(email)
        usr_password = passwordStrength(password)

        user = Users.query.filter_by(email=usr_email).first()
        if user:
            if check_password_hash(user.password, usr_password):
                flash('Logged in Successfully!', category='success')
                return redirect(url_for('dash.dashboard'))
            else:
                flash('Incorrect Password or Email.', category='warning')
        elif email == "" and password == "":
            flash('Please Input the required Fields', category='error')
        else:
            flash('Email Address Does Not Exist. Create A New Account', category='warning')
            return redirect(url_for('auth.usr_registeration'))
        
    return render_template('login.html')

@auth.route('/registeration', methods=['POST', 'GET'])
def usr_registeration():
    if request.method == 'POST':
        newUser_details = request.form
        username = newUser_details.get('username')
        usr_email = newUser_details.get('email')
        password = newUser_details.get('password')
        password2 = newUser_details.get('re-confirm')
        conditions = newUser_details.get('conditions')

        # email and password validators
        password1 = passwordStrength(password)
        email = validEmail(usr_email)

        user = Users.query.filter_by(email=email).first()
        # input validators
        if user:
            flash("User Already Exists!", category='error')
        elif username == "" or email == "" or password1 == "" or password2 == "":
            flash('Please Input The Required Fields', category='error')
        elif len(email) < 5:
            flash('Email Must Be Greater Than 4 Characters Long.', category='error')
        elif len(username) < 4:
            flash('Username Must Be Greater than 4 Characters.', category='error')
        elif password1 != password2:
            flash('Passwords DO NOT MUCH', category='error')
        elif len(password1) < 8:
            flash('Password Must Be atleast 7 Characters Long', category='error')
        elif not conditions:
            flash('Your must agree to our terms and conditions', category='error')
        # adding valid users to database
        else:
            newUser = Users(username=username, email=email, password=generate_password_hash(password1, method='sha256'))
            db.session.add(newUser)
            db.session.commit()
            flash('New User Created Successfully!', category='success')
            return redirect(url_for('auth.usr_login'))
        
    return render_template('register.html')