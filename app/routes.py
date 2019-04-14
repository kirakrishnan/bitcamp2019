from flask import render_template, request
from app import app
from .logic import final_case

@app.route('/')
def index():
    user = {'username': 'aravind'}
    return render_template('index.html', title = 'Employee Assistance', user = user)


@app.route('/result', methods = ['POST', 'GET'])
def result():
    if request.method == 'POST':
        form_fields = request.form
        salary = final_case(form_fields)

        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import numpy as np
        import matplotlib.pyplot as plt

        objects = ('Without', 'EmpMatch', 'Current', 'Increased by 3')
        # objects = ('Without Contributions', 'employer match', 'Current Contributions', 'Increased Contributions')
        y_pos = np.arange(len(objects))
        performance = salary

        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title('Smarter Investmenter Strategies')

        plt.savefig('app/static/histogram.jpg')
        plt.show()

        result = {"a": 1, "b": 2}
        return render_template("result.html", result = result)


