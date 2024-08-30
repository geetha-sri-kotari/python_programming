# used to store data in key-value pair forms
# kays can be of immutable types only
# do not allow duplicate keys
# using key, we can access values
# key-value pair must be written in the following form
# key : Value
# EX = {"j.k.Rowling" : "Harry Potter", "Abdul kalam" : "Wings of fire"}
# above is an example of a string : string dictionary
# Ex : {"a":1, "b":2, "c":3}
# above is an example for string : int dictionary

# creating a dictionary on own
# string : int mapping
d = {"sachin" : 100, "kohli" : 80, "ponting" : 78}
print(d)
print(type(d))
print(d["kohli"])      # gives the value associated eith "kohli"

# constructing from an empty dictionary
d = {}      # empty dictionary
d["sachin"] = 100         # inserts a new key-value pair "sachin" : 100
d["kohli"] = 80
d["kohli"] = 110           # updates 80 to 110
print(d)

# taking input from user
no_of_pairs = int(input("enter how many number of pairs you want to store : "))
d = {}
for i in range(no_of_pairs):
    key = input("enter a batsman name : ")
    value = int(input("enter number of centuries scored : "))
    d[key] = value           # creating a new key-value pair
print(d)

# constructing a dictionary from existing data
batsmen = ["sachin", "kohli", "ponting"]
centuries = [100, 80, 70]
d = {}
for i in range(len(batsmen)):
    d[batsmen[i]] = centuries[i]
print(d)