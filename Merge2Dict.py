dict1 = {'Ten': 10, 'Twenty': 20, 'Thirty': 30}
dict2 = {'Thirty': 30, 'Fourty': 40, 'Fifty': 50}
dict1.update(dict2)
print(dict1)
####other ways of merging dictionaries
'''
dict3={**dict1,**dict2}
dict3 = dict1|dict2
print(dict3)
dict3 =dict(dict1,**dict2) #** works only in dict2 not dict1
print(dict3)
dict3= collections.ChainMap(dict1,dict2) #this prints as chainMap
print(dict(dict3))
dict3=itertools.chain(dict1.items(),dict2.items())#this would print only address/refrence
print(dict(dict3))
dict3={k:v for i in(dict1,dict2) for k,v in i.items()} # straight forward with loops
print(dict3)
'''


