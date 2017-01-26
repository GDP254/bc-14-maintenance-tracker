# views.py

from flask import flash, render_template, session, redirect, url_for, request, abort

from app import app, db
from forms import SigninForm, RegisterForm, RegisterFacilityForm, UserForm, RegisterRequestForm, ProcessRequestForm
from models import User, Facility, Request
from flask_login import login_user, logout_user, login_required, current_user
from sms import send_sms

@app.route('/')
@login_required
def index():
	return redirect(url_for('view_users'))
    #return render_template("index.html")

@app.route('/user/signin', methods=['GET', 'POST'])
def signin():
	form = SigninForm()
	if form.validate_on_submit():
		usr = User.query.filter_by(email=form.email.data).first()
		if usr is not None and usr.verify_password(form.password.data):
			login_user(usr, form.remember.data)
			#send_sms('+254728696810', 'You just logged in!')
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
	return render_template("register.html", form=form, title="Register")

@app.route('/users/view')
@login_required
def view_users():
	users = User.query.all()
	return render_template("table_users.html", data=users)

@app.route('/user/<int:userid>/manage', methods=['GET', 'POST'])
@login_required
def manage_user(userid):
	usr = User.query.filter(User.id == userid).first()
	if usr is None:
		abort(404)
	form = UserForm()
	if form.validate_on_submit():
		usr.fname = form.fname.data
		usr.lname = form.lname.data
		usr.confirmed = form.confirmed.data
		usr.role = form.role.data
		db.session.add(usr)
		flash('User info has been updated')
		return redirect(url_for('view_users'))
	form.fname.data = usr.fname
	form.lname.data = usr.lname
	form.confirmed.data = usr.confirmed
	form.role.data = usr.role
	return render_template("register.html", form=form, title="User Information")

@app.route('/facility/register', methods=['GET', 'POST'])
@login_required
def register_facility():
	form = RegisterFacilityForm()
	if form.validate_on_submit():
		facility = Facility(name = form.name.data, status = form.status.data)
		db.session.add(facility)
		flash("You have created a facility")
		return redirect(url_for('index'))
	#Request facility details and set envroment variables
	return render_template("facility_register.html", form=form)

@app.route('/facilities/view')
@login_required
def view_facilities():
	facilities = Facility.query.all()
	return render_template("table_facilities.html", data=facilities)

@app.route('/facility/<facilityid>/manage', methods=['GET', 'POST'])
@login_required
def manage_facility(facilityid):
	facility = Facility.query.filter(Facility.id == facilityid).first()
	if facility is None:
		abort(404)
	form = RegisterFacilityForm()
	if form.validate_on_submit():
		facility.name = form.name.data
		facility.status = form.status.data
		db.session.add(facility)
		flash("You have updated a facility")
		return redirect(url_for('view_facilities'))
	form.name.data = facility.name
	form.status.data = facility.status
	#Request facility details and set envroment variables
	return render_template("facility_register.html", form=form)

@app.route('/request/register', methods=['GET', 'POST'])
@login_required
def register_request():
	form = RegisterRequestForm()
	if form.validate_on_submit():
		req = Request(name=form.name.data,
			notes=form.notes.data,
			facility_id=form.facility.data,
			#photo=form.photo.data,
			user_id=current_user.id)
		db.session.add(req)
		return redirect(url_for('index'))
	#Request facility details and set envroment variables
	return render_template("request_register.html", form=form, title="Register Requests")

@app.route('/requests/view')
@login_required
def view_requests():
	requests = Request.query.all()
	return render_template("table_requests.html", data=requests)

@app.route('/request/<requestid>/process', methods=['GET', 'POST'])
@login_required
def process_request(requestid):
	req = Request.query.filter(Request.id == requestid).first()
	if req is None:
		abort(404)
	form = ProcessRequestForm()
	if form.validate_on_submit():
		req.status = form.status.data
		req.admin_comment = form.comments.data
		req.assignee_name = form.contact_name.data
		req.assignee_number = form.contact_phone.data
		req.admin_id = current_user.id
		db.session.add(req)
		if req.status == 'approved':
			send_sms(req.assignee_number, 'req: '+str(req.id)+' at'+req.facility.name)
		else:
			#notify user
			pass
		flash('Request processed')
		return redirect(url_for('view_requests'))
	form.status.data = req.status
	form.comments.data = req.admin_comment
	form.contact_name.data = req.assignee_name
	form.contact_phone.data = req.assignee_number
	#Request facility details and set envroment variables
	return render_template("request_register.html", form=form, title="Process Requests")

