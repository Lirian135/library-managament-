from flask import Flask, redirect, render_template, flash, url_for
from flask_login import LoginManager, login_user, login_required, logout_user, current_user

from library import app
from library import db
from library.forms import *
from library.models import *



@app.route('/')
@app.route('/index')
def home():
    return 'Home'

@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    if form.validate_on_submit():
        student = Students.query.filter_by(username= form.username.data).first()
        if student:
            if check_password_hash(student.password_hash, form.password.data):
                login_user(student, remember=form.remember_me.data)
                return redirect(url_for('dashboard'))

    return render_template('login.html', form=form)

@app.route('/logout')
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/register', methods=['POST', 'GET'])
def register():
    form = RegisterForm()
    
    if current_user.is_authenticated:
        return redirect(url_for("dashboard"))
    
    if form.validate_on_submit():
        hashed_password = generate_password_hash(form.password.data, method='sha256')
        new_user = Students(username=form.username.data, email=form.email.data, password_hash=hashed_password)
        db.session.add(new_user)
        db.session.commit()
        
        return redirect(url_for('login'))
    
    return render_template('register.html', form=form)


@app.route('/dashboard')
@login_required
def dashboard():
    return render_template('dashboard.html', name=current_user.username)

@app.route('/user/<username>') #

def users(username):
    
    user = Students.query.filter_by(username=username).first()
    
    return render_template('profilePage.html', user=user)
    

    