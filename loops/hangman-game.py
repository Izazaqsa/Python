import random
fruits = ["apple","grapes","mango","banana","dates","cherry","apricot","orange","watermelon","peach"]
lives = 6 
rand_name = random.choice (fruits)

# for the spaces to print 
display =[]
for i in rand_name:
    display.append ("_")
print (display)
 
# for guessing the letter and comparing it with the word : 
game_over = False   # flag that will stop the loop if the value == True 
while not game_over: 
    guess_letter = input ("Guess the letter : ").lower()
    for position in range (len (rand_name)):    # the loop iterate as much as the chosen word size 
        letter = rand_name[position]    # the position is used to access every letter of the word and assign it to the letter
        if (guess_letter == letter ):    # check if the guess  letter is equal to the letter in the actual word or not   
            display [position]= guess_letter  # if yes than the display list is updated with that letter in the corresponding position as it have in the acutal word 
    print (display)    
    if guess_letter not in rand_name :   # use of member ship operator : check if the guess letter is in the actual word or not 
        lives = lives -1    # if not than decrement the lives with -1 
        print (f"\nyou have {lives} lives left : ")
        if (lives == 0 ):   
            game_over = True   # when lives == 0 mean you can't play further so the flag flip and you will lose the game
            print ("you lose")
    if '_' not in display :    # check whether the dashes _ are in the list or not if not than  you guess all the letter correctly and the game is over
        game_over= True 
        print ("you won")