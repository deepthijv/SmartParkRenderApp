from .extensions import db 

class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstname = db.Column(db.String(50))
    lastname=db.Column(db.String(50))
    phone=db.Column(db.Integer(20))
    email=db.Column(db.String(50))