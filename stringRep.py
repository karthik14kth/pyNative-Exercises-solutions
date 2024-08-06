str1 = "/*Jon is @developer & musician!!"
str=" "

for i in range(0,len(str1)):
    if str1[i].isalnum() or str1[i].isspace():
        str+=str1[i]
    else:
        str+="#"

print(str)