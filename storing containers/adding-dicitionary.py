students = students = [
    {
        'name':'Aizaz',
        'roll no': 32,
        'age':21, 
        'course':['pythom','c++','java']
    },

    {
        'name':'Yasir',
        'roll no ': 2,
        'age':21,
        'course':'web developing'
    },

    {
        'name':'Ali',
        'roll no ':26,
        'age':20,
        'course':'UI/UX'
    }
]


def add_new (name , roll_no, age, course):
    new_student ={}
    new_student['name']=name
    new_student['roll_no']=roll_no
    new_student['age']= age 
    new_student['course']=course
    students.append (new_student)


student_name= input ("enter the name : ")
std_rollno= int (input ("enter the roll no :"))
std_age = int (input ('enter the age :'))
std_course = input ("enter the course name : ")

add_new (name = student_name, roll_no=std_rollno , age = std_age, course = std_course)

print (students)