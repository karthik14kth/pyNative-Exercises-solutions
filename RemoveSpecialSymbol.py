str1 = "/*Jon is @developer & musician"
str2=" "
for i in range(0,len(str1)):
    if str1[i].isalnum() or str1[i].isspace():
        str2+=str1[i]
print(str2)