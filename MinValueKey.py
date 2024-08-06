sample_dict = {
  'Physics': 82,
  'Math': 65,
  'history': 75
}

a=min(sample_dict.values())

for i in sample_dict.keys():
    if sample_dict[i] == a:
        print("The key is:",i)


