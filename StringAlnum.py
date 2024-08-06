import re
str1 = "Emma25 is Data scientist50 and AI Expert"
#a=re.findall(r'[a-zA-Z0-9]+',str1)
a= str1.split(" ")

for i in range(0,len(a)):
    if re.findall(r'[0-9]+',a[i]):
        print(a[i])
