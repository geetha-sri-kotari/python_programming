# immutable
# cannot change the content once created
# used in hashing due to their immutable nature

t = (10, 20, 30)
print(type(t))
print(t[1])

# trying to change the values

# t[1] = 200
# gives error
# count, index -> functions on tuple
tup = (10, 20, 30)
print(tup.index(30))
print(tup.count(1))