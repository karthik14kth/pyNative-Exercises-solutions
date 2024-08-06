s1=input("enter the string")
s2=input("Enter the second string")
len1=len(s1)

if len1%2!=0:
    len2 =int((len1 +1)/2)
    s3= s1[0:len2]+s2+s1[len2:len1]
    print(s3)
else:
    len2 =int(len1/2)
    s3=s1[0:len2]+s2+s1[len2:len1]
    print(s3)
