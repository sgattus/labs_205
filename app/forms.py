from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])
    name = StringField('Name', validators=[DataRequired()])

    animalBio = TextAreaField('Animal Bio', validators=[DataRequired()])
    animalBehavior = TextAreaField('habitat', validators=[DataRequired()])
    extermination = TextAreaField('Extermination', validators=[DataRequired()])
    location = TextAreaField('Location', validators=[DataRequired()])

    submit = SubmitField('Create')


