# for testing purpose
# sal={"salary": 90000,
#      "retirement": 4,
#      "hsa": 4,
#      "fsa": 5,
#      "shares": 0,
#      "state": "VA",
#      "withholding": "single"
#      }

def salary_calculator(result):
    net = int(result['salary'])
    salary_inhand = net
    benefits = 0

    #contributions or benefits
    for benefit in [result['retirement'], result['hsa'], result['fsa'], result['shares']]:
        benefits = benefits + (int(result['salary']) * int(benefit) / 100)

    net = net - benefits

    #With holdings
    if result['withholding'] == 'single':
        std_deduction = 12200
    elif result['withholding'] == 'married-filing-jointly':
        std_deduction = 24400
    elif result['withholding'] == 'married-filing-separately':
        std_deduction = 12200
    elif result['withholding'] == 'head-of-household':
        std_deduction = 18350

    gross_income = float(net - std_deduction - benefits)

    #Federal taxes
    if gross_income < 9526 and gross_income > 0:
        fed_tax = 10
    elif gross_income < 38701 and gross_income > 9526:
        fed_tax = 12
    elif gross_income < 82501 and gross_income > 38701:
        fed_tax = 22
    elif gross_income < 157501 and gross_income > 82501:
        fed_tax = 24
    elif gross_income < 200001 and gross_income > 157501:
        fed_tax = 32
    elif gross_income < 500000 and gross_income > 200001:
        fed_tax = 35
    elif gross_income < 500000 or gross_income == 500000:
        fed_tax = 37


    #State taxes
    if result['state'] == 'VA':
        if gross_income < 3000 and gross_income >0:
            state_tax = 2
            salary_inhand = net - (gross_income * fed_tax / 100) - (gross_income * state_tax / 100)
        elif gross_income < 5000 and gross_income >3000:
            state_tax = 3
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income-3000) * state_tax / 100) - (3000 * 2 / 100)
        elif gross_income < 17000 and gross_income >5000:
            state_tax =5
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income-5000) * state_tax / 100) - (5000 * 3 / 100)
        elif gross_income > 17000 or gross_income == 17000:
            state_tax = 5.75
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income-17000) * state_tax / 100) - (17000 * 5 / 100)
    elif result['state'] == 'MD':
        if result['withholding'] == 'single':
            if gross_income < 1000 and gross_income > 0:
                state_tax = 2
                salary_inhand = net - (gross_income * fed_tax / 100) - (gross_income * state_tax / 100)
            elif gross_income < 2000 and gross_income > 1000:
                state_tax = 3
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 3000) * state_tax / 100) - 20
            elif gross_income < 3000 and gross_income > 1999:
                state_tax = 4
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 50
            elif gross_income < 100000 and gross_income > 2999:
                state_tax = 4.75
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 90
            elif gross_income < 125000 and gross_income > 99999:
                state_tax = 5
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 4697.50
            elif gross_income < 150000 and gross_income > 124999:
                state_tax = 5.25
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 5,947.50
            elif gross_income < 250000 and gross_income > 149999:
                state_tax = 5.5
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 7,260
            elif gross_income > 249999:
                state_tax = 5.75
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 12,760
        else:
            if gross_income < 1000 and gross_income > 0:
                state_tax = 2
                salary_inhand = net - (gross_income * fed_tax / 100) - (gross_income * state_tax / 100)
            elif gross_income < 2000 and gross_income > 1000:
                state_tax = 3
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 3000) * state_tax / 100) - 20
            elif gross_income < 3000 and gross_income > 1999:
                state_tax = 4
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 50
            elif gross_income < 150000 and gross_income > 2999:
                state_tax = 4.75
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 90
            elif gross_income < 175000 and gross_income > 149999:
                state_tax = 5
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 7072.50
            elif gross_income < 225000 and gross_income > 174999:
                state_tax = 5.25
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 8322.50
            elif gross_income < 300000 and gross_income > 224999:
                state_tax = 5.5
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 10947.50
            elif gross_income > 299999:
                state_tax = 5.75
                salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 15072.50

    elif result['state'] == 'DC':
        if gross_income < 10000 and gross_income > 0:
            state_tax = 4
            salary_inhand = net - (gross_income * fed_tax / 100) - (gross_income * state_tax / 100)
        elif gross_income < 40000 and gross_income > 9999:
            state_tax = 6
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 3000) * state_tax / 100) - 400
        elif gross_income < 60000 and gross_income > 3999:
            state_tax = 6.5
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 2200
        elif gross_income < 350000 and gross_income > 59999:
            state_tax = 8.5
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 3500
        elif gross_income < 1000000 and gross_income > 349999:
            state_tax = 8.75
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 28150
        elif gross_income > 1999999:
            state_tax = 8.95
            salary_inhand = net - (gross_income * fed_tax / 100) - ((gross_income - 5000) * state_tax / 100) - 85025

    net_value = salary_inhand
    for benefit in [result['retirement'], result['hsa'], result['fsa'], result['shares']]:
        net_value = net_value + (int(result['salary']) * int(benefit) / 100)
    return net_value


# print(salary_calculator(sal))
