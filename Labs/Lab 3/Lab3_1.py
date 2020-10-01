'''
Netti Welsh
Fall2020 CS5001
Problem 1
Buying a house
Calculating how long it will take to save for downpayment
'''

def down_payment(cost):
    '''
     Function: down_payment
        calculates the down_payment
     Parameters:
        cost -- the cost of house
     Returns
        returns the down payment in dollar amount
    '''
    down_payment = (cost * 25) / 100
    return down_payment


def saves_per_month(salary, saving):
    '''
     Function: saves_per_month
        calculates how much the user saves per month
        based on salary and the percentage user wants to save
     Parameters:
        salary -- the input salary
        saving -- a float of how much the user wants to save
     Returns
        returns the amount a user will save per month
    '''
    return (salary * saving) / 12

def main():
    cost = int(input("Cost Of House: "))
    salary = int(input("Salary: "))
    saving = float(input("Savings:"))


    months_until_downpayemnt = down_payment(cost) / saves_per_month(salary, saving)
    years_until_down_payment = int(months_until_downpayemnt // 12)
    months_until_downpayemnt = round(months_until_downpayemnt % 12)
    save_per_m = '{:.2f}'.format(saves_per_month(salary, saving))


    print(f'If you save ${save_per_m}, it will take {years_until_down_payment} years and {months_until_downpayemnt} months to save enough for the down payment')


if __name__ == "__main__":
    main()