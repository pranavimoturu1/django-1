from datetime import datetime
from flask_sqlalchemy import SQLAlchemy
from manage import app, db


class ContactUsModel(db.Model):
    id = db.Column('id', db.Integer, primary_key=True)
    name = db.Column('name', db.String)
    email = db.Column(db.String, unique=True, nullable=False)
    creation_date = db.Column('creation_date', db.Date, default=datetime.utcnow)