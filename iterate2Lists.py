list1 = [10, 20, 30, 40]
list2 = [100, 200, 300, 400]
list3 =[]
for i in range(len(list2)-1,-1,-1):
    list3.append(list2[i])

if len(list1) == len(list3):
    for i in range(0,len(list3)):
        print(str(list1[i])+" "+str(list3[i]))
