import random
class EmployeeWage():

    wage_per_hour=20
    full_day_hour=8
    part_time_day_hour=4
    month_days=20
    max_hour_per_month=100
    
    @classmethod
    def check_attendance(cls):
        return random.choice([0,1,2])

    @classmethod
    def calculate_daily_wage(cls):
        return cls.wage_per_hour*cls.full_day_hour

    @classmethod
    def part_time_employee_daily_wage(cls):
        return cls.part_time_day_hour*cls.wage_per_hour

    @classmethod
    def calculate_monthly_wage_for_20days_Max100hrs(cls):
        total_hours = 0
        total_days = 0
        total_wage =0
        while total_hours < cls.max_hour_per_month and total_days < cls.month_days:
            attendance = cls.check_attendance()
            if attendance == 1:
                total_hours += cls.full_day_hour
                total_wage += cls.calculate_daily_wage()
            elif attendance == 2:
                total_hours += cls.part_time_day_hour
                total_wage += cls.part_time_employee_daily_wage()
            else :
                total_hours += 0
                total_wage += 0
            total_days +=1
        return total_days, total_hours, total_wage
     
        

if __name__=='__main__':
    print("***Welcome to Employee Wage Computation Program***")
    total_days, total_hours, total_wages = EmployeeWage.calculate_monthly_wage_for_20days_Max100hrs()
    print(f"Employee Total Present Days in Month : {total_days} ")
    print(f"Employee Total Working Hours in Month : {total_hours} ")
    print(f"Employee Total Wages for one Month  : {total_wages} ")

    