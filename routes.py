# app/routes.py
from flask import render_template, url_for, flash, redirect
from app import app, db
from app.forms import RegistrationForm, LoginForm
from app.models import User, Appointment, Patient, MedicalRecord

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/register", methods=['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        user = User(username=form.username.data, email=form.email.data, password=form.password.data)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return render_template('register.html', title='Register', form=form)

@app.route("/login", methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        # Implement login logic
        flash('Login successful!', 'success')
        return redirect(url_for('home'))
    return render_template('login.html', title='Login', form=form)

@app.route("/appointment/new", methods=['GET', 'POST'])
def new_appointment():
    # Logic for creating a new appointment
    return render_template('appointment.html')
