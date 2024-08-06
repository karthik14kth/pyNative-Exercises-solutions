str1=input("enter the string")
strLen= len(str1)
str =" "
NewString= " "
if strLen%2 !=0:
    print("odd String")
    str=str1[0]+str1[int(strLen/2)]+str1[-1]
    print(str)
    NewString =str1[int(strLen/2-1)]+ str1[int(strLen/2)]+str1[int(strLen/2+1)]
    print("NewString for odd string:",NewString)
else:
    print("even string")
    str=str1[0]+str1[int(strLen/2-1)]+str1[int(strLen/2)]+str1[-1]
    print(str)
    NewString= str1[int(strLen/2-1)]+str1[int(strLen/2)]
    print("NewString for even string:",NewString)

