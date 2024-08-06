list1 = [10, 20, [300, 400, [5000, 6000], 500], 30, 40]
list1[2][2].append(7000)
print(list1)


#refrence for understanding sublist
print(list1[2])#inner sublist after main list
print(list1[2][2])# print inner most sublist

#
'''
#prints inner most list with errors
for i in range(0,len(list1)):
    for j in range(0,len(list1)):
        for k in range(0,len(list1)):
            try:
                print(list1[i][j][k])
                index = list1.index(6000,0,len(list1))
                print(index)
            except Exception as error:
                pass
                a=1

if a==1:
    print("Not all lists are sub lists and errors occured")


list2=[]
list3 =[]
for i in range(0,len(list1)):
  if type(list1[i]) == list:
      list2.append(list1[i])

print(list2)
'''