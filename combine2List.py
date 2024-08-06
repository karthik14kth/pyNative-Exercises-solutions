list1 = ["Hello ", "take "]
list2 = ["Dear", "Sir"]
print(list1[0]+list2[0])
list3=[]

if len(list1) == len(list2):
    for i in range(0,len(list1)):
        for j in range(0,len(list2)):
            list3.append(list1[i]+list2[j])
else:
    print("enter equal list elements")


print(list3)