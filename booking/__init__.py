from flask import Flask
from flask_sqlalchemy import SQLAlchemy
from flask_bootstrap import Bootstrap
from flask_bcrypt import Bcrypt
from flask_login import LoginManager



app=Flask(__name__,template_folder="TEMPLATES")
app.config['SECRET_KEY'] = 'ed6a264d3d2d25f1061fbea8588d36f5'
app.config['SQLALCHEMY_DATABASE_URI'] = "postgresql://airline_booking_user:eZp329AqLaaO4BjBci6sZCxPtvEesSdR@dpg-ci1a2ju7avjfjalqh5q0-a.oregon-postgres.render.com/airline_booking"
# app.config['SQLALCHEMY_DATABASE_URI'] ="postgresql://airline_booking_user:eZp329AqLaaO4BjBci6sZCxPtvEesSdR@dpg-ci1a2ju7avjfjalqh5q0-a/airline_booking"
db = SQLAlchemy(app)
bootstrap = Bootstrap(app)
bcrypt=Bcrypt(app)
login_manager = LoginManager(app)
login_manager.login_view = 'login'
from booking import routes  