import random 
wage_per_hour=20
full_day_hour=8
part_time_day_hour=4
month_days=20
max_hour_per_month=100
def check_attendance():
    return random.choice([0,1,2])

def calculate_daily_wage():
    return wage_per_hour*full_day_hour

def part_time_employee_daily_wage():
    return part_time_day_hour*wage_per_hour

def calculate_monthly_wage_for_20days_Max100hrs():
    total_hours = 0
    total_days = 0
    total_wage =0
    while total_hours < max_hour_per_month and total_days < month_days:
        attendance = check_attendance()
        if attendance == 1:
            total_hours += full_day_hour
            total_wage += calculate_daily_wage()
        elif attendance == 2:
            total_hours += part_time_day_hour
            total_wage += part_time_employee_daily_wage()
        else :
            total_hours += 0
            total_wage += 0
        total_days +=1
    return total_days, total_hours, total_wage
     
        

if __name__=='__main__':
    print("***Welcome to Employee Wage Computation Program***")
    total_days, total_hours, total_wages = calculate_monthly_wage_for_20days_Max100hrs()
    print(f"Employee Total Present Days in Month : {total_days} ")
    print(f"Employee Total Working Hours in Month : {total_hours} ")
    print(f"Employee Total Wages for one Month  : {total_wages} ")

    