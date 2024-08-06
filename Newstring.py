str1=input("Enter first string")
str2=input("Enter a second string")
str3=" "

if len(str1) > len(str2):
    i =len(str2)
    str4 = str1[i:]
    str = str2[0:i][::-1]
else:
    i= len(str1)
    str4 = str2[i:]
    str=str2[0:i][::-1]

for i  in  range (0,i,1):
    str3 += str1[i]+str[i]

print(str3+str4)
