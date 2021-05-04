from library import db, login, app

from werkzeug.security import generate_password_hash, check_password_hash

from flask_login import UserMixin

from flask_admin import Admin
from flask_admin.contrib.sqla import ModelView

@login.user_loader
def load_user(id):
    return Students.query.get(int(id))

class Books(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    author = db.Column(db.String)
    title = db.Column(db.String)
    description = db.Column(db.String)
    comments = db.relationship('Comments', backref='book')
    
    

class Students(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20), unique=True)
    email = db.Column(db.String(64), unique=True)
    password_hash = db.Column(db.String(50))
    
class Comments(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    comment_text = db.Column(db.String)
    perent = db.Column(db.Integer, db.ForeignKey('books.id'))
        
    

admin = Admin(app, name='library', template_mode='bootstrap3')
admin.add_view(ModelView(Students, db.session))
admin.add_view(ModelView(Books, db.session))
admin.add_view(ModelView(Comments, db.session))
    
    