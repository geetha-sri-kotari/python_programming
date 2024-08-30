# mainting frequency of iterables using dictionaries

s = "abaabcdcaba"
d = {}
for i in s:
    if i in d:
        d[i] += 1
    else :
        d[i] = 1
print(d)