from flask import Flask, render_template, request
app=Flask(__name__)

@app.route("/gundamRating", methods=["GET", "POST"])
def gundamRatingPage():
    if request.method == "POST":
        nameOfGundam = request.form.get('nameOfGundam', '').strip()
        price = request.form.get('price', '').strip()
        grade = request.form.get('grade', '').strip()
        scale = request.form.get('scale', '').strip()
        manualComprehensibility = request.form.get('manualComprehensibility', '').strip()
        buildFunness = request.form.get('buildFunness', '').strip()
        if not nameOfGundam or not price or not grade or not scale or not manualComprehensibility or not buildFunness:
            error = "Please fill in all required fields."
            return render_template('gundamForm.html', error=error)
        return render_template("gundamFormSuccess.html", nameOfGundam=nameOfGundam, price=price, grade=grade, scale=scale, manualComprehensibility=manualComprehensibility, buildFunness=buildFunness)
    return render_template("gundamForm.html")