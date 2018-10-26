from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField,SelectField,SelectMultipleField,DateField
from wtforms.validators import ValidationError, DataRequired, Email, EqualTo
from app.models import User


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    password = PasswordField('Password', validators=[DataRequired()])
    remember_me = BooleanField('Remember Me')
    submit = SubmitField('Sign In')


class AnimalForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])
    animalBio = StringField('Animal Bio', validators=[DataRequired()])
    #habitatName = StringField('habitat', validators=[DataRequired()])
    #climate = StringField('climate', validators=[DataRequired()])
    #food = StringField('food', validators=[DataRequired()])
    extermination = StringField('Extermination', validators=[DataRequired()])
    #location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Sign In')
    #sLocation = SelectField('Locations',validators=[DataRequired()], id='select_location')
    #sAnimal = SelectMultipleField('Animal(s)',validators=[DataRequired()], id='select_animal')
    year = DateField('Year of Extinction', validators=[DataRequired()])

class HabitatForm(FlaskForm):
    sLocation = SelectField('Locations',validators=[DataRequired()], id='select_location')
    sAnimal = SelectMultipleField('Animal(s)',validators=[DataRequired()], id='select_animal')
    climate = StringField('climate', validators=[DataRequired()])
    food = StringField('food', validators=[DataRequired()])
    habitatName = StringField('habitat', validators=[DataRequired()])
    submit = SubmitField('Sign In')

class LocationForm(FlaskForm):
    location = StringField('Location', validators=[DataRequired()])
    submit = SubmitField('Sign In')





class RegistrationForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    email = StringField('Email', validators=[DataRequired(), Email()])
    password = PasswordField('Password', validators=[DataRequired()])
    password2 = PasswordField(
        'Repeat Password', validators=[DataRequired(), EqualTo('password')])
    submit = SubmitField('Register')

    def validate_username(self, username):
        user = User.query.filter_by(username=username.data).first()
        if user is not None:
            raise ValidationError('Please use a different username.')

    def validate_email(self, email):
        user = User.query.filter_by(email=email.data).first()
        if user is not None:
            raise ValidationError('Please use a different email address.')
