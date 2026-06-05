class University :
    def __init__(self,uni_name):
        self.university_name = uni_name

    def show_details (self):
        print (f"univerisity name : {self.university_name}")
    
class Course (University):
    def __init__(self,course_name,uni):
        University .__init__(self, uni)
        self.course_name = course_name

    def show_details(self):
        print (f"course name : {self.course_name}")

class Branch (University) :
    def __init__(self,branch_name):
        self.branch_name = branch_name
    
    def show_details(self):
        print (f"branch name : {self.branch_name}")

class Faculty (Branch) :
    def __init__(self,faculty_name,Uni_name,Branch_name):
        University.__init__(self,Uni_name)
        Branch.__init__(self,Branch_name)
        self.faculty_name = faculty_name

    def show_details(self):
        University.show_details(self)
        Branch.show_details(self)
        print (f"faculty name : {self.faculty_name}")
        
class Student (Course , Branch) :
    def __init__(self,std_name,Course_name, Branch_name,uni_name):
        Course.__init__(self , Course_name,uni_name)
        Branch.__init__(self,Branch_name)
        self.student_name = std_name

    def show_details (self):
        print (f"student name : {self.student_name}")

fac1 = Faculty ('computer science','AWKUM','Garden')
fac1.show_details()

std1 = Student ('izaz',"python","Garden",'Awkum')
print (std1.course_name)

# crs = Course ('c++','awkum')
# print (crs.university_name)