list1=["Emma", "Jon", "", "Kelly", None, "Eric", ""]
list2=[]
for i in range(0,len(list1)):
    if (type(list1[i]) == str) and (list1[i]!= '') :
        #print(list1[i],end=' ')
        list2.append(list1[i])
print(list2)
