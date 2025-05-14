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

from datetime import datetime

class Review(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    mechanic_id = db.Column(db.Integer, db.ForeignKey('mechanic.id'), nullable=False)
    reviewer_name = db.Column(db.String(100))
    rating = db.Column(db.Float)  # 0.0 to 5.0
    comment = db.Column(db.Text)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    mechanic = db.relationship('Mechanic', backref=db.backref('reviews', lazy=True))
