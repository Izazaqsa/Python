list1 = [ "😀", "😀", "😀"]
list2 = [ "😀", "😀", "😀"]
list3 = [ "😀", "😀", "😀"]
matrix = [list1 , list2 , list3]
print (f"{list1}\n{list2}\n{list3}")
position = input ("enter the position where you want to hide your money : ")
row = int (position [0])   # the first number is for the row 
column = int (position [1])   # the second number is for the column 
selected_row = matrix [row -1]   #this tells that the selected row in matrix is row-1 because of the indexing start from 0
selected_row [column -1] = "X"    # this tell that the column is in that row and column - 1 because of the indexing
print (f"{list1}\n{list2}\n{list3}")
