from flask import render_template, request
from app import app

@app.route('/')
def index():
    user = {'username': 'aravind'}
    return render_template('index.html', title = 'Employee Assistance', user = user)


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        result = request.form
        return render_template("result.html", result = result)