import random 
def check_attendance():
    return random.choice([0,1])

if __name__=='__main__':
    print("Welcome to Employee Wage Computation Program")
    attendance=check_attendance()
    if attendance==1:
        print('Employee is present')
    elif attendance==0:
        print('Employee is absent')
