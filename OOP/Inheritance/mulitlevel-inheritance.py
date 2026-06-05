class Principal:
    def __init__(self,name):
        print ('init from principal class')
        self.school_name= name

    def manage (self):
        print ('i can manage all of the events happening in the school')

class Teacher (Principal) :
    def __init__(self, class_name,shcl_name):
        Principal.__init__(self,shcl_name)
        print ('init from teacher class')
        self.headmaster = class_name

    def teach(self):
        print ('i can teach all of the subject related to science ')

class Student (Teacher) : 
    def __init__(self,std_name,cls_name,shcl_name):  # one parameter for itself , one for the teacher class and one for the principal class 
        Teacher.__init__ (self,cls_name,shcl_name)   # takes two parameter cause the principal inint function call there and it needs one parameters
        print ('init from student class')
        self.student_name = std_name

    def learning (self):
        print ('i can learn anything if i want it with true heart')

    def introduction(self):
        print (f"Hi i am {self.student_name} , i read in class {self.headmaster} , my school name is {self.school_name}")

std1= Student ('izaz','10th','the knowledge school')
std1.introduction ()
std1.teach()
print (Student.mro())   # print the way of execution of the code in the classes 
  



""" actually if dont mention the inint function in the other classes so only one of them will be called on object creation 
because a single constructor can be called on object creation but if you have to call all of the init functions from every class so you have to mention it 
in the derived class or like  i did in the above code and you to  passes the required parameters also to fullfill there
needs or it will give an error  """