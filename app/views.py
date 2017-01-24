# views.py

from flask import render_template, session, redirect, url_for

from app import app, db
from forms import SigninForm, RegisterForm, RegisterFacilityForm
from models import User, Facility

@app.route('/')
def index():
    return render_template("index.html")

@app.route('/user/signin', methods=['GET', 'POST'])
def signin():
	form = SigninForm()
	if form.validate_on_submit():
		session['name'] = form.email.data
		return redirect(url_for('index'))
	return render_template("signin.html", form=form)

@app.route('/user/register', methods=['GET', 'POST'])
def register_user():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(fname = form.fname.data,
					lname = form.lname.data,
					email = form.email.data,
					password = form.password.data)
		db.session.add(user)
		return redirect(url_for('signin'))
	return render_template("register.html", form=form)

@app.route('/facility/register', methods=['GET', 'POST'])
def register_facility():
	form = RegisterFacilityForm()
	if form.validate_on_submit():
		#Model mainipulation
		pass
		return redirect(url_for('index'))
	#Request facility details and set envroment variables
	return render_template("facility_register.html", form=form)
