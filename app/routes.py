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


import random
from io import BytesIO
# from StringIO import StringIO  # python 2.7x

from flask import Flask, make_response
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure


@app.route('/plot.png')
def plot():
    fig = Figure()
    axis = fig.add_subplot(1, 1, 1)

    xs = range(100)
    ys = [random.randint(1, 50) for x in xs]
    axis.plot(xs, ys)
    canvas = FigureCanvas(fig)
    output = BytesIO()
    # output = StringIO()  # python 2.7x
    canvas.print_png(output)
    response = make_response(output.getvalue())
    response.mimetype = 'image/png'
    return response