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
    ticket= db.relationship("Ticket", backref="User")
    def __repr__(self):
        return f"User('{self.id}','{self.name}', '{self.email}')"

class Admin(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(20), nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(60), nullable=False)
    
    def __repr__(self):
        return f"User('{self.name}', '{self.email}')"

class Ticket(db.Model,UserMixin):

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    flight_id=db.Column(db.Integer,db.ForeignKey('flight.id'),nullable=False)
    passenger = db.Column(db.Integer, nullable=False)
    cost=db.Column(db.Integer,nullable=False)

    # relation to user
    def __repr__(self):
        return f"Ticket('{self.id}','{self.user_id}', '{self.passenger}', '{self.cost}','{self.User}')"

class Flight(db.Model,UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100), nullable=False)
    date = db.Column(db.Date, nullable=False)
    time = db.Column(db.Integer,nullable=False)
    form= db.Column(db.String(100), nullable=False)
    to = db.Column(db.String(100), nullable=False)
    cost= db.Column(db.Integer,nullable=False)
    seat= db.Column(db.Integer,nullable=False,default=0)
    ticket= db.relationship("Ticket", backref="Flight")

    def __repr__(self):
        return f"flight('{self.id}','{self.name}',' {self.date}','{self.seat}','{self.time}','{self.form}','{self.cost}','{self.to}')"