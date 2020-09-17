'''
Netti Welsh
Fall2020 CS5001
Problem 2
Buying a house
Calculating how long it will take to save for downpayment
'''
def main():
    cost = int(input("Cost Of House: "))
    salary = int(input("Salary: "))
    saving = float(input("Savings:"))

    down_payment = (cost * 25) / 100
    saves_per_month = (salary * saving) / 12
    months_until_downpayemnt = down_payment / saves_per_month
    years_until_down_payment = int(months_until_downpayemnt // 12)
    
    months_until_downpayemnt = round(months_until_downpayemnt % 12)

    save_per_m = '{:.2f}'.format(saves_per_month)
    

    print(f'If you save ${save_per_m}, it will take {years_until_down_payment} years and {months_until_downpayemnt} months to save enough for the down payment')

 
if __name__ == "__main__":
    main()    