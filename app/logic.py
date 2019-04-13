
sal={"salary": 2000,
     "retirement": 4,
     "hsa": 0,
     "fsa": 0,
     "shares": 0,
     "state": "VA"
     }


def salary_calculator(result):
    net = int(result['salary'])
    for benefit in [result['retirement'], result['hsa'], result['fsa'], result['shares']]:
        net = net - (int(result['salary']) * int(benefit) / 100)
    if result['state'] == 'VA':
        tax = 5.3
    elif result['state'] == 'MD':
        tax = 5.75
    elif result['state'] == 'VA':
        tax = 8.95
    salary_inhand = net - (float(result['salary']) * tax / 100)
    return salary_inhand


# print(salary_calculator(sal))