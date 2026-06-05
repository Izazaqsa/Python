weight = float (input("enter your weight in kg: "))
height = float (input("enter your height in meter: "))
BMI = weight / (height **2)
print (f"your BMI is {BMI:.2f}")
if (BMI<18.5):
    print("you are underweight")
elif (BMI>=18.5 and BMI<=24.9):
    print("you have normal weight")
elif (BMI>=25 and BMI<=29.9):
    print("you are overweight")
else :
    print ("you are obese")