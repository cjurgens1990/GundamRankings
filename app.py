from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timezone
app=Flask(__name__)

app.secret_key='top-secret'

app.config['SQLALCHEMY_DATABASE_URI']='sqlite:///gundams.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS']=False

db=SQLAlchemy(app)

class Profile(db.Model):
    id=db.Column(db.Integer, primary_key=True)
    nameOfGundam=db.Column(db.String(50), nullable=False)
    price=db.Column(db.Integer, nullable=False)
    grade=db.Column(db.String(5), nullable=False)
    scale=db.Column(db.String(5), nullable=False)
    manualComprehensibility=db.Column(db.Integer, nullable=False)
    buildFunness=db.Column(db.Integer, nullable=False)
with app.app_context():
    db.create_all()

@app.route("/", methods=["GET", "POST"])
def gundamRatingPage():
    if request.method == "POST":
        nameOfGundam = request.form.get('nameOfGundam', '').strip()
        price = request.form.get('price', '').strip()
        grade = request.form.get('grade', '').strip()
        scale = request.form.get('scale', '').strip()
        manualComprehensibility = request.form.get('manualComprehensibility', '').strip()
        buildFunness = request.form.get('buildFunness', '').strip()

        if not nameOfGundam or not price or not grade or not scale or not manualComprehensibility or not buildFunness:
            error="Please fill in all required fields"
            return render_template('gundamForm.html', error=error)
        try:
            new_profile=Profile(
                nameOfGundam=nameOfGundam, 
                price=int(price), 
                grade=grade, 
                scale=scale, 
                manualComprehensibility=int(manualComprehensibility), 
                buildFunness=int(buildFunness)
            )
            db.session.add(new_profile)
            db.session.commit()
        except Exception as e:
            db.session.rollback()
            error="An error has occurred while saving your Gundam Stats. Get good loser."
            return render_template('gundamForm.html', error=error)
        return render_template("gundamFormSuccess.html", nameOfGundam=nameOfGundam, price=price, grade=grade, scale=scale, manualComprehensibility=manualComprehensibility, buildFunness=buildFunness)
    return render_template("gundamForm.html")



@app.route('/admin/profiles')
def admin_profiles():
    profiles=Profile.query.all()
    return render_template('adminProfile.html', profile=profiles)