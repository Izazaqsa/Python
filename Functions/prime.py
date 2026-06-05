def is_prime (num):
    for i in range (2, num):
        if (num % i== 0):
            print (f"the {num} is not a prime number ")
            return 
    print (f"the {num} is prime number ")

number  = int (input ("enter a number : "))
is_prime(number)