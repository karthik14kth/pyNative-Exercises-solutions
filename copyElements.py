tuple1 = (11, 22, 33, 44, 55, 66)
tuple2=(tuple1[3],tuple1[4])
print('tuple2:',tuple2)

#Author's solution'
tuple2=tuple1[3:-1]
print(tuple2)