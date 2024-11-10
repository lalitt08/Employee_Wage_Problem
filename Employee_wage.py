import random 
wage_per_hour=20
full_day_hour=8
part_time_day_hour=4
def check_attendance():
    return random.choice([0,1,2])

def calculate_daily_wage():
    return wage_per_hour*full_day_hour

def part_time_employee_daily_wage():
    return part_time_day_hour*wage_per_hour

if __name__=='__main__':
    print("Welcome to Employee Wage Computation Program")
    attendance=check_attendance()
    if attendance==1:
        print('Employee is present')
        print(f'Employee daily wage: {calculate_daily_wage()}')
    elif attendance==2:
        print(f'Employee works part time and there daily wage is {part_time_employee_daily_wage()}')
    elif attendance==0:
        print('Employee is absent')
