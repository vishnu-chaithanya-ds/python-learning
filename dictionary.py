############ DICTIONARYS........(GET),,(UPDATE),,,(VALUES),,(KEYS),,,(ITEMS),,,,


# d={2:'nani',66:'anantapur',}

# print(d.get(2))

# print(d.values())

# print(d.items())

# print(d.keys())

# d.update({222:444})
# print(d)


#### USING FOR LOOP IN DICIONARY,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,,

# for i in {4:'nani',66:'hellokingstar','mysore':4}:
#     print(i)


for i,j in {88:'nani',66:'mysore','music':88}.items():
    print(i,j)

# ACCESS BOTH KEYS AND VALUES USING ITEMS() FROM DICT

details={"name":"nani","roll":37}
for i,j in details.items():
    print(i,j)

