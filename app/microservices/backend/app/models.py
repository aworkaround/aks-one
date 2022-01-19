from datetime import datetime
from app import db

class SimpleTable(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(40), nullable=False)
    email_id = db.Column(db.String(60), nullable=False)
    year_of_birth = db.Column(db.String(4), nullable=False)
    age_group = db.Column(db.String(20), nullable=False, default='Unknown')
