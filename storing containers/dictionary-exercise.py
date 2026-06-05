students = {
    'Ali': 92,
    'Sara': 85,
    'Zain': 76,
    'Areeba': 63,
    'Hamza': 58,
    'Fatima': 48,
    'Bilal': 34,
    'Usman': 70,
    'Hira': 88,
    'Kiran': 95
}


# the program that convert the marks of the students from the one dictionary to grades in another dictionary 

students_grade = {}

for name in students :
    if students [name] > 90 :
        students_grade[name]= 'A+'
    elif students [name]> 80 : 
        students_grade[name]= 'A'
    elif students [name]>70 :
        students_grade [name]= 'B'
    elif students [name]>60 :
        students_grade [name]= 'C'
    else :
        students_grade[name]='Fail'

print (students_grade)