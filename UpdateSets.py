set1 = {10, 20, 30, 40, 50}
set2 = {30, 40, 50, 60, 70}
set1=set1.union(set2)-set1.intersection(set2)
#set1.symmetric_difference_update(set2) #Autthor's solution
print(set1)

