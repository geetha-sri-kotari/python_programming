# set is an unordered collection immutable objects
# sets will not hold duplicates
# set elements are enclosed within curly braces
# mutable
# elements ca be changed even after creation
# not subscriptable( are not indexed )
# set elements can't be of mutable types, which means
   # you can have a set of integers , set of strigs, set of floats
   # but you cannot have set of lists, set of sets
   # as lists and sets are mutable

# set if integers
s1 = {10, 20, 30, 10, 30, 20}
print(s1, type(s1))
# set of strings
s2 = {"abc", "xyz", "abc"}
print(s2, type(s2))
# set of lists
   # s3 = {[10, 20,], [10, 20]}
   # print(s3, type(s3))

e1 = (6, 6)
e2 = (6, 6)
e3 = (7, 8)
e4 = (7, 8)
set_of_end_points = {e1, e2, e3, e4}
print(set_of_end_points)
print(len(set_of_end_points))

# set methods

# set.add() -> used to add 1 element to set
s4 = {10, 20, 30}
s4.add(40)       # added at starting
s4.add(10)
print(s4)

s = {}      # will not create empty set, but creates dictionary
s = set()   # creates an emtpy set
print(type(s))

n = int(input())
for i in range(n):
    student_name = input()
    s.add(student_name)
print(s)

# straight lines
n = int(input("enter no of lines : "))
set_of_start_points = set()
set_of_end_points = set()
for i in range(n):
    start_point = tuple(map(int, input().split()))
    end_point = tuple(map(int, input().split()))
    set_of_start_points.add(start_point)
    set_of_end_points(end_point)
print(set_of_start_points, len(set_of_start_points))
print(set_of_end_points, len(set_of_end_points))

# set() function - converts others iterables into s set
#                - string, list, range(), tuple can be converted to a set

# converting a list to a set
c = ["c", "C++", "Java", "Java", "Java", "C++", "Python"]
s = set(c)
print(s)

# set of instructions

# converting a string into a set
x = "abaccghjirjswwww"
s = set(x)
print(s)

# set.remove() - used to remove an element from a set
#              - element based removal
#              - if the element is not present in the set it throws error
s1 = {10, 20, 30, 40, 50}
s1.remove(40)
print(s1)

# st.discard() -> remove the element if it is present, if it is not present it does not throw any error
s1.discard(100)
print(s1)
s1.discard(50)
print(s1)

# union() -> set A set B
# intersection() -> common elements in set A and et B
# difference(A, B) -> elements in A but not in B
# difference(B, A) -> elements in B but not in A
# symmetric_difference() -> all elements from A and B except intersection

s1 = {10, 20, 30}
s2 = {30, 40, 50}
print(s1.union(s2))     # 10 20 30 40 50
print(s1.intersection(s2))    # 30
print(s1.difference(s2))      # 10 20
print(s2.difference(s1))      # 40 50
print(s1.symmetric_difference(s2))   # 10 20 40 50

# s1.intersection_update(s2) -> s1 is changed to s1 intersection s2

# how to read a set :

s = set(map(int, input().split()))
print(s)