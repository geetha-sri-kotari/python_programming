d = {'sachin' : 100, 'kohli' : 80, 'ponting' : 77}
print(len(d))
for i in d :
    print(i)               # prints only key

for i in d :
    print(i, d[i])         # prints both key and value

print(d.keys())            # list of keys

print(d.values())          # list of values

print(d.items())           # list of items
