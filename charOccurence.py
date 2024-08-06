str1= input("Enter the string")
dict= {}
for i in range(0,len(str1)):
    if str1.count(str1[i]) == 1:
        dict[str1[i]]=str1.count(str1[i])
    else:
        dict[str1[i]]=str1.count(str1[i])

print(dict.items())

