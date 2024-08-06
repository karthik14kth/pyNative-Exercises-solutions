str1 ='I am 25 years and 10 months old'
str2 =" "
for i in range (0,len(str1)):
    if str1[i].isdigit():
        str2+=str1[i]
print(str2)