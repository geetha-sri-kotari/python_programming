# value based looping

movies = ['kalki', 'bahubali', 'rebel']
for each in movies:
    print(each)

# index based looping

names = ['walter', 'jessie', 'saul', 'skyler']
for i in range(4):
    print(names[i])

# printing in backward direcion
for j in range(len(names)-1, -1, -1):
    print(names[j], end = ' ')

# removing an item from a list  - pop, remove, clear

# pop() -  deletes last element from list by default
#       -  returns removed element
#       - can mention index for popping
#       - default index is -1
nums = [10, 20, 30, 40, 50, 10, 10]
nums.pop()      # removes 50 from the list
nums.pop(0)     # removes 0th index element

# use a list as a stack
# append()
# pop()
stack = []
stack.append(10)
stack.append(20)
stack.append(30)
recent_element = stack.pop()
# checking stack is empty
if stack:
    print("Not emoty")
else :
    print("Empty")

# pop on empty list leads to runtime error

# remove()   - element based removal
#            - first occurence of element from left
nums.remove(10)

# removing all occurences of a element in a list
while 10 in nums:
    nums.remove(10)

# clear()
# deletes all elements from list by leaving empty list
nums.clear()
print(nums)

# In-Place utlity operations

# reverse()
# reverse the list in place
# return type - none
num = [10, 20, 30]
print(f"Before reversing {num}" )
num.reverse()
print(f"After reverse: {num}")

# sort()
# sorts elements in-place
# setting reverse = True sorts list in descending order
nums = [5, -2, 4, 67, -4]
nums.sort()
print(nums)
nums.sort(reverse=True)      # by default reverse is set false
print(nums)

# sort using key

# sorting based on no of vowels
def get_vowel_count(string):
    vowels = 'aeiou'
    cnt = 0
    for i in string:
        if i in vowels:
            cnt += 1
    return cnt
names = ['skyler', 'walter', 'jessie', 'siaul']
names.sort(key=get_vowel_count)                      # ascending order of no of vowels
names.sort(key=get_vowel_count, reverse=True)        # descending order of no of vowels

# copy()
# returns shallow copy of list
a = [10, 20, 30]
# Deep copy
b = a                  # a and b are pointing to same list
print(a, b)
print(id(a), id(b))                    # id() - gives address

b = a.copy()                      # shallow copy of a

# Utility methods

# index() - left most index of value in list
print(nums.index(30))

# count()
print(nums.count(10))