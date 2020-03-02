from models.settings import db
from datetime import datetime


class Machine_models(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String) 
    power = db.Column(db.Integer)
    voltage = db.Column(db.Integer)
    current = db.Column(db.Integer)
    picture = db.Column(db.String)
    thikness = db.Column(db.String)
    text = db.Column(db.String)
    session_token = db.Column(db.String)
    created = db.Column(db.DateTime, default=datetime.utcnow)