from flask_wtf import FlaskForm
from wtforms.fields import DateField
from wtforms import  StringField , IntegerField, SubmitField ,DateField,PasswordField,BooleanField,TimeField,SelectField
from wtforms.validators import DataRequired, Length, Email, EqualTo, ValidationError
from booking.model import User
from datetime import date

class Flights(FlaskForm):
        dep = SelectField("From",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()])
        arv = SelectField("To",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()])
        depDate = DateField('deptDate', validators=[DataRequired()], format='%Y-%m-%d',default=date.today())
        retDate = DateField('retDate', format='%Y-%m-%d')
        adult =IntegerField("Adult",validators=[DataRequired()],default=1)
        child = StringField("Child",validators=[DataRequired()],default=0)
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
        def validate_phone(self,phone):
                    user = User.query.filter_by(phone=phone.data).first()
                    if user:
                        raise ValidationError('That phone is taken. Please choose a different one.')


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
        to = SelectField("to",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()])
        form = SelectField("form",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()])
        name=StringField("name",validators=[DataRequired()])
        
        date=DateField("date",validators=[DataRequired()],default=date.today())
        time=IntegerField("time",validators=[DataRequired()])
        cost=IntegerField("Price",validators=[DataRequired()])
        submit=SubmitField("submit")
        
class RemoveFlight(FlaskForm):
        name=StringField("name",validators=[DataRequired()])
        to = SelectField("to",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()])
        form = SelectField("form",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] ,validators=[DataRequired()]   )
        
        date=DateField("date")
        time=IntegerField("time")
        submit=SubmitField("sumbit")    
    # x=datetime.datetime(1,1,1,1,1,1)

class SearchFlight(FlaskForm):
        name=StringField("name",validators=[DataRequired()])
        to = SelectField("to",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] )
        form = SelectField("form",choices=[("Chennai"),("Delhi"),("Mumbai"),("Hyderabad"),("Bangalore")] )
        date=DateField("date")
        time=IntegerField("time")
        submit=SubmitField("sumbit")    


