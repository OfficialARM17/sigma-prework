from datetime import datetime
def calculate_age(birthdate_str):
    birthdate = datetime.strptime(birthdate_str, "%d-%m-%Y")
    today = datetime.today()
    age = today.year - birthdate.year
    if(today.month, today.day) < (birthdate.month, birthdate.day):
        age -= 1
    return age

date1 = "01-01-1990"
date2 = "04-12-1972"

print("Age for {} is: {} years".format(date1, calculate_age(date1)))
print("Age for {} is: {} years".format(date2, calculate_age(date2)))