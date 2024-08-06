list1 = ["Mike", "", "Emma", "Kelly", "", "Brad"]
list2=[]

for i in range(0,len(list1)):
    if list1[i].isalnum() != False:
        list2.append(list1[i])

print(list2)