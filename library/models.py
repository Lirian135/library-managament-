from library import db, login

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin


@login.user_loader
def load_user(id):
    return Students.query.get(int(id))

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String)
    description = db.Column(db.String)
    

class Students(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(50))
    #d
    
    
    
    

    
    