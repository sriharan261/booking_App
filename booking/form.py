from flask_wtf import FlaskForm
from wtforms import  StringField , IntegerField, SubmitField ,DateField,PasswordField,BooleanField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from booking.model import User


class Flights(FlaskForm):
    dep = StringField( "From", validators=[DataRequired()])
    arv = StringField("To",validators=[DataRequired()])
    depDate = DateField('deptDate', validators=[DataRequired()], format='%Y-%m-%d')
    retDate = DateField('retDate', format='%Y-%m-%d')
    adult =StringField("Adult")
    child = StringField("Child")
    submit = SubmitField('search')


class RegistrationForm(FlaskForm):
    name = StringField('name',
                           validators=[DataRequired(), Length(min=2, max=20)])
    email = StringField('Email',
                        validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    phone=IntegerField("Phone",validators=[ DataRequired()])
    confirm_password = PasswordField('Confirm Password',
                                     validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Sign Up')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user:
            raise ValidationError('That email is taken. Please choose a different one.')

class LoginForm(FlaskForm):
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit=SubmitField("login")

class LoginAdminForm(FlaskForm):
    email=StringField('email',validators=[DataRequired()])
    password=PasswordField("password",validators=[DataRequired()])
    remember = BooleanField('Remember Me')

    submit=SubmitField("login")

class AddFlight(FlaskForm):
    name=StringField("name",validators=[DataRequired()])
    form=StringField("form",validators=[DataRequired()])
    to=StringField("to",validators=[DataRequired()])
    date=DateField("date",validators=[DataRequired()],format='%Y-%m-%d')
    time=IntegerField("time",validators=[DataRequired(),Length(min=4,max=4)])
    sumbit=SubmitField("submit")
    
class RemoveFlight(FlaskForm):
    name=StringField("name",validators=[DataRequired()])
    form=StringField("form")
    to=StringField("to")
    date=DateField("date",format='%Y-%m-%d')
    time=IntegerField("time",validators=[Length(min=4,max=4)])
    sumbit=SubmitField("submit")    

class SearchFlight(FlaskForm):
    name=StringField("name",validators=[DataRequired()])
    form=StringField("form")
    to=StringField("to")
    date=DateField("date",format='%Y-%m-%d')
    time=IntegerField("time",validators=[Length(min=4,max=4)])
    sumbit=SubmitField("submit")    


