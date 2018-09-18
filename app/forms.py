from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, SubmitField, TextAreaField
from wtforms.validators import DataRequired


class LoginForm(FlaskForm):
    username = StringField('Username', validators=[DataRequired()])

    animalBio = TextAreaField('Animal Bio', validators=[DataRequired()])
    animalBehavior = TextAreaField('Animal Behavior', validators=[DataRequired()])
    extermination = TextAreaField('Extermination', validators=[DataRequired()])

    submit = SubmitField('Create')


