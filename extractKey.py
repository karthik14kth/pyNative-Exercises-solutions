sample_dict = {
    "name": "Kelly",
    "age": 25,
    "salary": 8000,
    "city": "New york"}


if 'name' in sample_dict and 'salary' in sample_dict:
    a=sample_dict.get('name','name not present')
    b=sample_dict.get('salary','salary not present')
else:
    a= None
    b=None
    print("the keys are not present")


new_dict={'name':a,'salary':b}
print(new_dict)
