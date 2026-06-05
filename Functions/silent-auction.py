import os

def bid_data ():
    bid_list ={}
    flag = True
    while flag :
        name = input ("enter the name : ")
        bid  = int (input ("enter the bid amount : "))
        bid_list[name]=bid
        option= input ("does anyone want to bid (yes or no)").lower ()
        if option == 'yes':
            os.system ('cls')
        elif option == 'no':
            flag = False 
            highest_price = 0
            winner = ''
            for bidder in bid_list :
                if highest_price < bid_list[bidder] :
                    highest_price = bid_list[bidder]
                    winner = bidder
            print (f"the name is {winner} with a bid price : {highest_price}")

    print (f"the bid list is {bid_list}")
                               
   
bid_data()