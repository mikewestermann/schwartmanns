from models.settings import db
from datetime import datetime


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    Vorname = db.Column(db.String) 
    Nachname = db.Column(db.String)
    Name_des_Unternehmens = db.Column(db.String)
    Position_im_Unternehmen = db.Column(db.String)
    Email_Adresse = db.Column(db.String, unique=True)
    password_hash = db.Column(db.String)
    session_token = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)
