import random 
wage_per_hour=20
full_day_hour=8
def check_attendance():
    return random.choice([0,1])

def calculate_daily_wage():
    return wage_per_hour*full_day_hour

if __name__=='__main__':
    print("Welcome to Employee Wage Computation Program")
    attendance=check_attendance()
    if attendance==1:
        print('Employee is present')
        print(f'Employee daily wage: {calculate_daily_wage()}')
    elif attendance==0:
        print('Employee is absent')
