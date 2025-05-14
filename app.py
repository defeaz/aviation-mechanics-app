from flask import Flask, render_template, request, redirect, url_for
from models import db, Mechanic
import os

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db.init_app(app)

with app.app_context():
    db.create_all()

@app.route('/')
def index():
    query = request.args.get('location', '')
    if query:
        mechanics = Mechanic.query.filter(Mechanic.location.ilike(f"%{query}%")).all()
    else:
        mechanics = Mechanic.query.all()
    return render_template('index.html', mechanics=mechanics)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        m = Mechanic(
            name=request.form['name'],
            location=request.form['location'],
            services=request.form['services'],
            contact=request.form['contact']
        )
        db.session.add(m)
        db.session.commit()
        return redirect(url_for('index'))
    return render_template('register.html')

@app.route('/mechanic/<int:mechanic_id>')
def mechanic_detail(mechanic_id):
    mechanic = Mechanic.query.get_or_404(mechanic_id)
    return render_template('mechanic_detail.html', mechanic=mechanic)

@app.route('/mechanic/<int:mechanic_id>/review', methods=['POST'])
def submit_review(mechanic_id):
    reviewer_name = request.form['reviewer_name']
    rating = float(request.form['rating'])
    comment = request.form['comment']

    new_review = Review(
        mechanic_id=mechanic_id,
        reviewer_name=reviewer_name,
        rating=rating,
        comment=comment
    )
    db.session.add(new_review)
    db.session.commit()

    return redirect(url_for('mechanic_detail', mechanic_id=mechanic_id))
