# dict() is the built-in function to create dictionary
# dict() expects iterable of iterables where inner iterable are of length 2

data = [["sachin", 100], ["kohli", 80], ["ponting", 77]]
d = dict(data)
print(d)

data1 = [("sachin", 100), ("kohli", 80), ("ponting", 77)]
d = dict(data1)
print(d)

data2 = [{"sachin", 100}, {"kohli", 80}, {"ponting", 77}]
d = dict(data2)
print(d)

data3 = ['a1', 'b2', 'c3']
d = dict(data3)
print(d)