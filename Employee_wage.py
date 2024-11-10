import random 
wage_per_hour=20
full_day_hour=8
part_time_day_hour=4
month_days=20
def check_attendance():
    return random.choice([0,1,2])

def calculate_daily_wage():
    return wage_per_hour*full_day_hour

def part_time_employee_daily_wage():
    return part_time_day_hour*wage_per_hour

def calculate_monthly_wage():
    total_daily_wage = []
    for _ in range(month_days):
        attendance = check_attendance()
        if attendance == 1:
            total_daily_wage.append(calculate_daily_wage())
            
        elif attendance == 2:
            total_daily_wage.append(part_time_employee_daily_wage())
        else :
            total_daily_wage.append(0)
    return sum(total_daily_wage), total_daily_wage
        

if __name__=='__main__':
    print("***Welcome to Employee Wage Computation Program***")
    monthly_wage, day_wise_wage = calculate_monthly_wage()
    print(f"Given Employee monthly wages is : {monthly_wage}")
    print(f"Given Employee day wise monthly wages  : {day_wise_wage}")