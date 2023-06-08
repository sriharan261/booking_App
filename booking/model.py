from datetime import datetime
from booking import db,login_manager
from flask_login import UserMixin


@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))



class User(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    phone = db.Column(db.String(10),unique=True,nullable=False)
    password = db.Column(db.String(60), nullable=False)
    ticket= db.relationship("Ticket", backref="Ticket",lazy=True)
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Admin(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Ticket(db.Model):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_id=db.Column(db.Integer,db.ForeignKey('flight.id'),nullable=False)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Integer,nullable=False)
    adult = db.Column(db.Integer, nullable=False)
    kid = db.Column(db.Integer, nullable=False)

    # relation to user
    def __repr__(self):
        return f"Ticket('{self.name}', '{self.date}', '{self.adult}','{self.kid}')"

class Flight(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Integer,nullable=False)
    form= db.Column(db.String(100), nullable=False)
    to = db.Column(db.String(100), nullable=False)
    seat= db.Column(db.Integer,nullable=False,default=0)
    ticket= db.relationship("Ticket", backref="user",lazy=True)

    def __repr__(self):
        return f"Ticket('{self.name}', '{self.date}', '{self.date}','{self.time}','{self.form}','{self.to}')"