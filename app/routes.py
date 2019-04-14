from flask import render_template, request
from app import app
from .logic import final_case

form_fields_global = {}
@app.route('/')
def index():
    user = {'username': 'aravind'}
    return render_template('index.html', title = 'Employee Assistance', user = user)


# @app.route('/result', methods = ['POST', 'GET'])
def result(salary,title,img_path):
    # if request.method == 'POST':
    #     form_fields = request.form
    #     salary = final_case(form_fields)
        if img_path == 'histogram.jpg':
            objects = ['Only 401k', '401k & HSA', '401k & FSA', '401k & Shares', '401k,HSA,FSA', '401k,HSA,Shares',
                       '401k,FSA,Shares', '401k,FSA,Shares']
            performance = []
            for key in objects:
                performance.append(salary[key])
        elif img_path == 'retirement.jpg':
            objects = ['Only 401k', '401k & HSA', '401k & FSA', '401k & Shares', '401k,HSA,FSA', '401k,HSA,Shares', '401k,FSA,Shares', 'EmpMatch', 'Current']
            performance = []
            for key in objects:
                performance.append(salary[key])
        elif img_path == 'hsa.jpg':
            objects = ['Only HSA', '401k & HSA', 'HSA & FSA', 'HSA & Shares', '401k,HSA,FSA', '401k,HSA,Shares', 'HSA,FSA,Shares', 'EmpMatch', 'Current']
            performance = []
            for key in objects:
                performance.append(salary[key])
        elif img_path == 'fsa.jpg':
            objects = ['Only FSA', '401k & FSA', 'HSA & FSA', 'FSA & Shares', '401k,HSA,FSA', '401k,FSA,Shares', 'HSA,FSA,Shares', 'EmpMatch', 'Current']
            performance = []
            for key in objects:
                performance.append(salary[key])
        elif img_path == 'shares.jpg':
            objects = ['Only Shares', '401k & Shares', 'HSA & Shares', 'FSA & Shares', '401k,HSA,Shares', '401k,FSA,Shares', 'HSA,FSA,Shares', 'EmpMatch', 'Current']
            performance = []
            for key in objects:
                performance.append(salary[key])


        import matplotlib
        matplotlib.use('TkAgg')
        import matplotlib.pyplot as plt
        plt.rcdefaults()
        import numpy as np
        import matplotlib.pyplot as plt
        y_pos = np.arange(len(objects))
        plt.bar(y_pos, performance, align='center', alpha=0.5)
        plt.xticks(y_pos, objects)
        plt.ylabel('Usage')
        plt.title(title)
        fig = plt.gcf()
        fig.set_size_inches(15,10, forward=False)
        fig.savefig('app/static/'+img_path)
        # fig.show()

        return None


@app.route('/result', methods = ['POST', 'GET'])
def call_result():
    if request.method == 'POST':
        form_fields = request.form
        salary = final_case(form_fields)
        for k,v in salary.items():
            form_fields_global[k]=v
        result(salary,'Smarter Investmenter Strategies', 'histogram.jpg')
    return render_template("result.html")

@app.route('/retirement', methods = ['POST', 'GET'])
def call_retirement():
    result(form_fields_global,'401K Contribution Details', 'retirement.jpg')
    return render_template("retirement.html")

@app.route('/hsa', methods = ['POST', 'GET'])
def call_hsa():
    result(form_fields_global,'HSA Contribution Details', 'hsa.jpg')
    return render_template("hsa.html")

@app.route('/fsa', methods = ['POST', 'GET'])
def call_fsa():
    result(form_fields_global,'FSA Contribution Details', 'fsa.jpg')
    return render_template("fsa.html")

@app.route('/shares', methods = ['POST', 'GET'])
def call_shares():
    result(form_fields_global,'Shares Contribution Details', 'shares.jpg')
    return render_template("shares.html")
