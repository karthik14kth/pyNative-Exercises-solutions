str1= input("enter the string")
str2=input("Enter the bigger string")

for i in range(0,len(str1),1):
    if str1[i] in str2:
        a= True
    else:
        a=False

if a==1:
    print("String is balanced")
else:
    print("String is not balanced")

