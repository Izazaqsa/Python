def leap_year (year):
    if (year%4 ==0 and year %100!=0):
        return True
    else :
        return False 
    
def days (year , name ):
    if leap_year(year) and month == 2 :
        return 29 
    if not leap_year(year) and month == 2:
        return 28 
    elif  month % 2 == 0 :
        return 30 
    elif  month % 2 != 0:
        return 31


year = int (input ("enter the year : "))
month = int (input ("enter the month : "))

print (f" {days (year, month)} days in {month} month ")