from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    services = db.Column(db.Text)
    contact = db.Column(db.String(100))
