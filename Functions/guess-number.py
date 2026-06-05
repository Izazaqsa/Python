import random 
print ('let me think between 1 to 50 ')
number = random.randint (1,51)

def To_guess (guess):

    guess_number = int (input("Make a guess : "))
    if  guess_number == number :
        print ('Congratulation ! you guess correct')
    elif guess_number != number and guess!=0:
        if guess_number < number :
            print ("your guess number is low ")
        elif guess_number > number :
            print ('your guess number is high ')
        print (f"you have {guess} left ")
        To_guess(guess-1)
    elif guess == 0 :
        print (f"you are out of guesses and you lose ! ")
        
print ("chose the level ( easy , hard ) : ")
level = input ("enter the level mode : ").lower()
if level == 'easy':
    To_guess(10) 
elif level == 'hard':
    To_guess(5)