class Teacher :
    def __init__(self,name, class_name, salary ):
        self.name = name 
        self._class_name = class_name    # this is protected   and this is accessible in their inherited class 
        self.__salary = salary # this is private 
    
    def display (self):
        print (f"hi my name is {self.name} and my salary is {self.__salary}")   #to make the private member accessible you to define inside the function of that class

class Student (Teacher):
    def __init__(self,rollno,name , class_name, salary ):
        super().__init__(name ,class_name , salary)
        self.rollno = rollno 

    def show (self):
        print (f"hi my name is {self.name } , i read in {self._class_name} and my roll  no is {self.rollno}")

std1 = Student(32,'izaz','5th sem', 250000)
std1.show()
# print (std1.__salary)  # this is not accessible outside of the class so this will show an error
# print(std1._class_name)  # this is also not accessible but in python it doesn't give any error so better to not use it 
std1.display()
print (std1._Teacher__salary)   # this is the technique use to access the private of the class outside of the class and it is known is name mangling 