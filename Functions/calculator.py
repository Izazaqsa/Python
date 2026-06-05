import os 
def calculate (num1 ,op , num2):
    if op == '+':
        return num1 + num2 
    elif op == '-':
        return num1 - num2
    elif op == '*':
        return num1 *num2
    elif op == '/':
        if num2 == 0 :
            print ("denumerator can't be zero ")
        else:
            return num1/num2

def calculator ():
    first_num = int (input ("enter the number : "))
    flag= True
    while flag:
        operator = input ("which operation you want to perform (/, *, +, -) : ")
        sec_num = int (input ("enter the second number : "))

        output =calculate( num1 = first_num ,op = operator , num2 = sec_num )
        result ={}
        if isinstance (output, (int, float )):
            result[operator]= output 


        print (f"{first_num} {operator} {sec_num} = {output} ")
        choose = input ("if want to continue with the previous {output} type 'y' , if not type 'n' or type 'x' to exit the  : ").lower ()
        if choose == 'y':
            flag = True
            first_num = output 
        elif choose == 'n':
            flag = False
            os.system ('cls')
            calculator ()
        elif choose =='x':
            flag = False  

calculator ()