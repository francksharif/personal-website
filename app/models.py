from . import db 
from werkzeug.security import generate_password_hash,  check_password_hash

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(64), index=True, unique=True, nullable=False)
    password_hash = db.Column(db.String(128), nullable=False)

    def set_password(self, password):
        self.password_hash = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
    



class Project(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(128), unique=True, nullable=False)
    small_description = db.Column(db.String(64),  nullable=False)
    description = db.Column(db.Text, nullable=False)
    image_file = db.Column(db.String(100), nullable=False)
    github_link = db.Column(db.String(100), nullable=False)
    project_link = db.Column(db.String(100), nullable=True)


    def __repr__(self):
        return f'{self.title}'