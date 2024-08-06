list1 = ["M", "na", "i", "Ke"]
list2 = ["y", "me", "s", "lly"]
list3=[]

if len(list1) == len(list2):
    for i in range(0,len(list1)):
        list3.append(list1[i]+list2[i])
else:
    print("This program works only in scenario where both list length are same")

print(list3)


