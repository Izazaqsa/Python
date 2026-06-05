# this is a dicitoinary with in a dictionary 
students_data = {
    'Aizaz':{'age':21, "address":'dir', 'course':['pythom','c++','java']},
    'Yasir':{'age':22, 'address':'mardan', 'course':'web developing'},
    'Ali':{'age':20, 'address':'mardan', 'course':'UI/UX'}
}

# this is dictionary inside a list 
students = [
    {
        'name':'Aizaz',
        'age':21, 
        "address":'dir', 
        'course':['pythom','c++','java']
    },

    {
        'name':'Yasir',
        'age':22,
        'address':'mardan',
        'course':'web developing'
    },

    {
        'name':'Ali',
        'age':20,
        'address':'mardan',
        'course':'UI/UX'
    }
]

# print (students_data["Aizaz"]['address'])   # will only access the address of the key (Aizaz)
# students_data['Aizaz']['phone_number']=1234   # adding another value to the dictionary 
# print (students_data) 
# print (students_data['Aizaz']['course'])  # this will print the list which is associated to the key course 
# print (students_data['Aizaz']['course'][1])   # this will print the item on the 1 index whic having the key course 

# print (students)   # print the whole list 
print (f"{students[0]}\n {students[1]}\n {students[2]}")  # print the dictionary on the indices 
