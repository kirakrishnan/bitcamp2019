from flask import render_template, request
from app import app
from .logic import salary_calculator

@app.route('/')
def index():
    user = {'username': 'aravind'}
    return render_template('index.html', title = 'Employee Assistance', user = user)


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        form_fields = request.form
        salary = salary_calculator(form_fields)
        result = {}
        for k, v in form_fields.items():
            result[k]=v
        result["TAKEHOME"] = salary
        return render_template("result.html", result = result)