from app import app, db
from flask_sqlalchemy import SQLAlchemy
from werkzeug.security import generate_password_hash, check_password_hash


class User(db.Model):
    id = db.Column("id", db.Integer, primary_key = True)
    username = db.Column(db.String(100))
    name = db.Column(db.String(100))
    email = db.Column(db.String(100))
    is_superuser = db.Column(db.Boolean())
    password = db.Column(db.String(128))

    def set_password(self, password):
        self.password = generate_password_hash(password)
    
    def check_password(self, password):
        return check_password_hash(self.password, password)
