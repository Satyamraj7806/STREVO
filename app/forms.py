from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import Length, EqualTo, Email, DataRequired, ValidationError




class RegisterForm(FlaskForm):
    username = StringField(label='Username',validators=[Length(min=5, max=30), DataRequired()])
    email_id = StringField(label='Email ID',validators=[Email(), DataRequired()])
    password1 = PasswordField(label='Password',validators=[Length(min=5, max=15), DataRequired()])
    password2 = PasswordField(label='Confirm Password', validators=[EqualTo('password1'), DataRequired()])
    Submit = SubmitField(label='Create Account')



class LoginForm(FlaskForm):
    username  = StringField( label = 'Username')
    password1 = PasswordField(label = 'Password')
    Submit = SubmitField(label = 'Submit')
