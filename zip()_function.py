# zip() is used to generate N length tuples, where ith element of each tuple comes from ith iterable

lst = [10, 20, 30, 40, 50]
string = "abc"
z = zip(lst, string)
print(list(z))

# zip stops generating tuples when smallest iterable is exhausted

# more than two iterables
z = zip([1, 2, 3, 4, 5], "money heist", range(10, 100, 10))
print(list(z))

# creating dict using zip
batsmen = ["sachin", "kohli", "ponting"]
centuries = [100, 80, 77]
d = dict(zip(batsmen, centuries))
print(d)
