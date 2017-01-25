# views.py

from flask import flash, render_template, session, redirect, url_for, request

from app import app, db
from forms import SigninForm, RegisterForm, RegisterFacilityForm
from models import User, Facility
from flask_login import login_user, logout_user, login_required, current_user

@app.route('/')
@login_required
def index():
    return render_template("index.html")

@app.route('/user/signin', methods=['GET', 'POST'])
def signin():
	form = SigninForm()
	if form.validate_on_submit():
		usr = User.query.filter_by(email=form.email.data).first()
		if usr is not None and usr.verify_password(form.password.data):
			login_user(usr, form.remember.data)
			return redirect(request.args.get('next') or url_for('index'))
		flash('Invalid username or password')
	return render_template("signin.html", form=form)

@app.route('/signout')
@login_required
def signout():
	logout_user()
	flash('You have been logged out.')
	return redirect(url_for('signin'))

@app.route('/user/register', methods=['GET', 'POST'])
def register_user():
	form = RegisterForm()
	if form.validate_on_submit():
		user = User(fname = form.fname.data,
					lname = form.lname.data,
					email = form.email.data,
					password = form.password.data,
					role = 'default')
		db.session.add(user)
		flash('You may now Sign In')
		return redirect(url_for('signin'))
	return render_template("register.html", form=form)

@app.route('/facility/register', methods=['GET', 'POST'])
@login_required
def register_facility():
	form = RegisterFacilityForm()
	if form.validate_on_submit():
		#Model mainipulation
		pass
		return redirect(url_for('index'))
	#Request facility details and set envroment variables
	return render_template("facility_register.html", form=form)
