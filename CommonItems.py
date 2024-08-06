set1 = {10, 20, 30, 40, 50}
set2 = {60, 70, 80, 90, 10}


if set1.isdisjoint(set2):    #Isdisjoint() check whether sets are disjoint (Learnt from Author)
    print("There is no common elemnts in two sets")
else:
    print("The common items are", set1.intersection(set2))
