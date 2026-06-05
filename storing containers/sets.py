# set1={2,4,6,True,"ali","izaz"}
# print (set1)
# #  print (set1[1])  # no indexing is possible , will give an error 
# # set1[3]=44# no modification to the existing elements because of the no indexing 
# set1.add (100)  # can add new elements
# set1.remove (2)   # removal is also possible
# print (set1)

# #set operations 

set1 = {1,3,4,5,6}
set2 = {4,3,7,8,9}
# union 
print (set1.union(set2))
# set1 | set2  

# intersection 
print (set1.intersection(set2))
# set1 & set2 

# Difference 
print (set1.difference (set2))
# set1-set2

# symmetric difference 
print (set1.symmetric_difference(set2))
# set1 ^ set2 

# Disjoint set 
print (set1.isdisjoint(set2))

# subset 
print (set1.issubset(set2))
# set1 <= set2

#superset 
print (set1.issuperset(set2))
# set1>= set2 