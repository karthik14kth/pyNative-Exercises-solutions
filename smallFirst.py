str=input("Enter an all alphabet string with atleast one capital letter:")
len= len(str)
new=" "
small =" "
big= " "
for i in range(0,len):
    if str[i].islower():
        small+=str[i]
    else:
        big+=str[i]
new = (small+big).replace(" ","")
print(new)


