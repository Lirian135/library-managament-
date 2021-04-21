from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField
from wtforms.validators import InputRequired, Email, Length, email_validator



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    remember_me = BooleanField('remember me')
    
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    

class BookForm(FlaskForm):
    book_author = StringField('book_author',validators=[InputRequired(), Length(min=3, max=25)] )
    title = StringField('title',validators=[InputRequired(), Length(min=3, max=25)])
    description = TextAreaField('textarea', validators=[InputRequired(), Length(min=25, max=250)])
    
    