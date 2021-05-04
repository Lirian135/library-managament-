from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, BooleanField, TextAreaField, SubmitField
from wtforms.validators import InputRequired, Email, Length, email_validator



class LoginForm(FlaskForm):
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Log In')
    
    
class RegisterForm(FlaskForm):
    email = StringField('email', validators=[InputRequired(), Email(message='Invalid email'), Length(max=50)])
    username = StringField('username', validators=[InputRequired(), Length(min=4, max=18)])
    password = PasswordField('password', validators=[InputRequired(), Length(min=8, max=50)])
    submit = SubmitField('Register')
    

class BookForm(FlaskForm):
    title = StringField('title',validators=[InputRequired(), Length(min=3, max=25)])
    description = TextAreaField('textarea', validators=[InputRequired(), Length(min=25, max=250)])
    submit = SubmitField('Add Book')
    
class CommentForm(FlaskForm):
    comment_text = StringField('comment_text',validators=[InputRequired(), Length(min=3, max=25)])
    submit = SubmitField('Add Comment')
    
    