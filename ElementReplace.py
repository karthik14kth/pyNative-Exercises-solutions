list1 = [5, 10, 15, 20, 25, 50, 20]
print(list1)

if list1.count(20) >=1:
    a=list1.index(20,0,len(list1))
else:
    print("The item is not present in the list")

list1.pop(3)
#list1.remove(20)
list1.insert(a,200)
print(list1)