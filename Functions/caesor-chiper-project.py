alphabets = [
    'a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm',
    'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']

# def encryption (plain_text , key):
#     cipher_text =""
#     for char in plain_text:
#         if char in alphabets:
#             position = alphabets.index (char)
#             new_position = (position+key) % 26
#             cipher_text += alphabets[new_position]
#         else : 
#             cipher_text += char 
#     print (f"the ecnrypted message is : {cipher_text}")

# def decryption (cipher_text,key):
#     plain_text = ""
#     for char in cipher_text:
#         if char in alphabets:
#             position = alphabets.index (char)
#             new_position = (position - key) % 26
#             plain_text += alphabets[new_position]
#         else : 
#             plain_text += char 
#     print(f"the decrypted message is: {plain_text}")

# flag = True 
# while flag :
#     choice = input ("Type encrypt for encryption and decrypt for decryption : \n")
#     message = input ("Type your message : \n")
#     shift_key = int (input ("enter the shift number  : \n"))
#     if choice == "encrypt":
#         encryption (plain_text=message , key = shift_key)
#     elif choice == "decrypt":
#         decryption (cipher_text = message , key = shift_key)
#     option = input ("to continue enter yes while enter no to quite : ").lower ()
#     if option == 'yes':
#         flag = True 
#     elif option == 'no':
#         flag = False



# the function are almost same but have a slight difference so one can also be created for it 

def operation (text , key, choice):
        cipher_text = ""                                                   # if choice == 'decrypt':
        for char in text :                                                 #   key = key*-1
            position = alphabets.index (char)         # for decryption the key will be negative while for the 
            if choice == 'encrypt':                   # the encryption it will remain positive this is the only differnce in it 
                new_position = (position + key) % 26
            elif choice == 'decrypt':
                new_position = (position-key)% 26
            cipher_text += alphabets[new_position]
        print (f"the encrypted message is : {cipher_text}")

flag =True
while flag :
    choice = input ("Type encrypt for encryption and decrypt for decryption : \n")
    message = input ("Type your message : \n")
    shift_key = int (input ("enter the shift number  : \n"))
    operation (text= message , key = shift_key , choice = choice )
    option = input ("to continue enter yes while enter no to quite : ").lower ()
    if option == 'yes':
        flag = True 
    elif option == 'no':
        flag = False

    

    
    




