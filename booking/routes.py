from flask import render_template,request,flash,redirect,url_for
from booking import app ,db ,bcrypt
from booking.form import Flights ,LoginForm,RegistrationForm,LoginAdminForm,AddFlight,RemoveFlight,SearchFlight
from booking.model import User,Flight,Ticket, Admin
from flask_login import login_user, current_user, logout_user, login_required

@app.route("/")
@app.route("/home")
def home():
      form=Flights()
      if form.validate_on_submit():
        name=Flight.query.find(name=form.name.data)
        date=Flight.query.find(name=form.name.data)
        to=Flight.query.find(name=form.name.data)
        form=Flight.query.find(name=form.name.data)

        flight =Flight.query.where(name and date and form and to)
        return render_template('flight,html',flights=flight)
      return render_template("home.html",form=form)

@app.route("/flight")
@login_required
def flight():
    user=User.query.filter(email=current_user.email).first()
    id=user.id
    flights=Ticket.query.filter(id)
    
    return render_template("flightSchedule.html",flight=flights,title="Flight")

@app.route("/register", methods=['GET', 'POST'])
def register():
    if current_user.is_authenticated:
        return redirect(url_for('home'))
    form = RegistrationForm()
    if form.validate_on_submit():
        hashed_password = bcrypt.generate_password_hash(form.password.data).decode('utf-8')
        user = User(name=form.name.data, email=form.email.data,phone=form.phone.data, password=hashed_password)
        db.session.add(user)
        db.session.commit()
        flash(f'Account created for {form.name.data}!', 'success')
        return redirect(url_for('login'))
    return render_template('register.html', title='Register', form=form)


@app.route("/login", methods=['GET', 'POST'])
def login():
    if current_user.is_authenticated:
            return redirect(url_for('home'))
    form = LoginForm()
    if form.validate_on_submit():
        user = User.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)

@app.route("/admin", methods=['GET', 'POST'])
def adminlogin():
    form = LoginAdminForm()
    if current_user.is_authenticated:
            return redirect(url_for('adminhome'))
    if form.validate_on_submit():
        user = Admin.query.filter_by(email=form.email.data).first()
        if user and bcrypt.check_password_hash(user.password, form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('home'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('login.html', title='Login', form=form)


@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")


@app.route("/add",methods=['GET', 'POST'])
def add():
    form=AddFlight()
    if form.validate_on_submit():
        flight =Flight(name=form.name.data, date=form.date.data,time=form.time.data, form=form.form.data ,to=form.to.data)
        db.session.add(flight)
        db.session.commit()
        return redirect(url_for('adminhome'))
    return render_template("add.html",form=form)


@app.route("/delete",methods=['GET', 'POST'])
def delete():
    form =RemoveFlight()
    if form.validate_on_submit():
            flight =Flight(name=form.name.data, date=form.date.data,time=form.time.data, form=form.form.data ,to=form.to.data)
            db.session.remove(flight)
            db.session.commit()
            return redirect(url_for('adminhome'))

    return render_template("delete.html",form=form)


@app.route("/search",methods=['GET', 'POST'])
def search():

    form=SearchFlight()
    if form.validate_on_submit():
        flight =Flight(name=form.name.data, date=form.date.data,time=form.time.data, form=form.form.data ,to=form.to.data)
        return render_template("serach.html",form=form,filghts=flight)
    return render_template("serach.html",form=form)

@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))