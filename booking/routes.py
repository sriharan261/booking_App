from flask import render_template,request,flash,redirect,url_for
from booking import app ,db ,bcrypt
from booking.form import Flights ,LoginForm,RegistrationForm,LoginAdminForm,AddFlight,RemoveFlight,SearchFlight
from booking.model import User,Flight,Ticket, Admin
from flask_login import login_user, current_user, logout_user, login_required


@app.route("/")
@app.route("/home",methods=['GET', 'POST'])
def home():
      form=Flights()
      (form)
      if form.validate_on_submit():
        date=form.depDate.data
        fom = form.dep.data
        to=form.arv.data
        count=int(form.adult.data)+int(form.child.data)
        flight =Flight.query.filter_by(form=fom,to=to,date=date).all()
        l=[]
        for i in flight:
             if i.seat+count< 61:   
                    l.append(i)
                    
        return render_template('flight.html',flights=l,c=count)
      return render_template("home.html",form=form)



@app.route("/flight",methods=['GET', 'POST'])
@login_required
def flight():
    user=current_user.id
    user=Ticket.query.filter_by(user_id=user).all()
    return render_template("flightSchedule.html",flights=user)


@app.route("/book/<flightid>&<c>",methods=['GET', 'POST'])
@login_required
def flightbooking(flightid,c):
    print(flightid,c)
    Userid=current_user.id
    flight=flightid
    passenger=int(c)
    t=Flight.query.filter_by(id=flight).first()
    s=t.seat
    print(s)
    t.seat=s+passenger
    print(t.seat)
    cost=t.cost
    cost=cost*passenger
    ti=Ticket(flight_id=flight,user_id=Userid,passenger=passenger,cost=cost)
    db.session.add(ti)
    db.session.commit()
    print(ti)
    print(t)
    return redirect(url_for("home")) 


@app.route("/myflight")
def myflight():
    return render_template("flightSchedule.html")


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
        login_user(user)
        return redirect(url_for('home'))
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
        if user and (user.password== form.password.data):
            login_user(user, remember=form.remember.data)
            next_page = request.args.get('next')
            return redirect(next_page) if next_page else redirect(url_for('adminhome'))
        else:
            flash('Login Unsuccessful. Please check email and password', 'danger')
    return render_template('admin.html', title='Login', form=form)



@app.route("/adminhome")
def adminhome():
    return render_template("adminhome.html")


@app.route("/add",methods=['GET', 'POST'])
def add():
    form=AddFlight()
    print(form.validate_on_submit())
    if form.validate_on_submit():
        name=form.name.data
        from1 =form.form.data
        to=form.to.data
        date=form.date.data
        print("Printing Date")
        time =form.time.data
        cost=form.cost.data
        flight =Flight(name=name,time=time,date=date,form=from1 ,to=to,cost=cost)
        db.session.add(flight)
        db.session.commit()
        return redirect(url_for('adminhome'))
    else:
            print('We messed up')
            name=form.name.data
            from1 =form.form.data
            to=form.to.data
            date=form.date.data
            print(name)
            print(from1)
            print(to)
            print(date)
            if form.errors != {}:
                for err in form.errors.values():
                    print(f"There was an error with creating user: {err}") 
    return render_template("add.html",form=form)


@app.route("/delete",methods=['GET', 'POST'])
def delete():
    form =RemoveFlight()
    if form.validate_on_submit():
            flight =Flight(name=form.name.data, date=form.date.data,time=form.time.data, form=form.form.data ,to=form.to.data)
            db.session.delete(flight)
            db.session.commit()
            return redirect(url_for('adminhome'))

    return render_template("delete.html",form=form)


@app.route("/search",methods=['GET', 'POST'])
def search():
    form=SearchFlight()
    print(form.validate_on_submit())
    name=form.name.data
    if form.validate_on_submit():
        name=form.name.data
        from1 =form.form.data
        to=form.to.data
        date=form.date.data
        print("Printing Date")
        time =form.time.data
        x=Flight.query.filter_by(name=name,form=from1,to=to,date=date,time=time).all()
        return render_template("serach.html",form=form,flights=x)
    elif(name):
            print('We messed up')
            name=form.name.data
            from1 =form.form.data
            to=form.to.data
            date=form.date.data
            time=form.time.data
            print(name)
            print(from1)
            print(to)
            print(date)
            flight=Flight.query.filter_by(name=name).order_by(Flight.date.desc()).all()
            if form.errors != {}:
                for err in form.errors.values():
                    print(f"There was an error : {err}")
            l=[]
            if(date):
                 for i in flight:
                    if(i.date==date and i not in l) :
                         l=l+[i]
            if(from1):
                 for i in flight:
                        if(i.form ==from1 and i not in l ):
                             l=l+[i]
            if(time ):
                 for i in l:
                    if(i.time==time and i not in l) :
                         l=l+[i]
            if(to ):
                 for i in flight:
                    if(i.to==to and i not in l) :
                         l=l+[i]
            if(flight ):
                 print(flight)
            else:
                 print("Failure")
            if(len(l)==0):
                 l=flight                
            for i in flight:
                 print(i.name)
            return render_template("serach.html",form=form,flights=l)
    return render_template("serach.html",form=form)


@app.route("/logout")
def logout():
    logout_user()
    return redirect(url_for('home'))