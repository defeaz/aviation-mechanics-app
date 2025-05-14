from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

class Mechanic(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    location = db.Column(db.String(100))
    services = db.Column(db.Text)
    qualifications = db.Column(db.Text)
    photo_url = db.Column(db.String(200))  # Link to an image
    bio = db.Column(db.Text)  # Personal statement

