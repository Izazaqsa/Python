years = 90 
current_age = int (input ("enter the current age: "))
left_years = years - current_age 
days = left_years * 365 
weeks = round ( days / 7 )
months = left_years * 12 

print (f"you have {days} days, {weeks} weeks and {months} months left ")