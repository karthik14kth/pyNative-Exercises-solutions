str1 = "PYnative29@#8496"
number=" "

for i in range(0,len(str1),1):
    if str1[i].isdigit():
        number+=str1[i]
#print(number)

a=number.split(" ")
for i in range(0,len(a)):
    if i.is_integer():
        integer=a[i]
digits= len(integer)
num=0
for j in range (0,len(integer)):
    quotient= int(integer)//10
    numb= int(integer)%10
    num+=numb
    integer=quotient

print("The sum is",num)
print("The average is",num/digits)
