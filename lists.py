# dynamic
# ordered
# indexed from 0
# square brackets should enclose list elemets
# separated using commas

x = [10, 20, 30, 40]
# ind 0   1   2   3
# ind -4  -3  -2  -1
print(len(x))
# x. gives many methos
# to add : append, insert, extend

# append - used to add one elemnt at a time to existing list and adds element at the end
x.append(50)
print(x)

n = int(input("Enter size of array: "))
ls = []
# taking input in next line
for i in range(n):
    ele = int(input())
    ls.append(ele)
print(ls)
# taking input using space i.e., same line
n1 = int(input())
ls1 = list(map(int, input().split()))     # reads any number of elements
ls2 = list(map(int, input().split()))[:n]      # reads only n elements
print(sum(ls2))

# insert - takes two values 1.index and 2.element
x.insert(0, 30)
x.insert(1, 'hello')

# extend - takes an iterable and appends every element of iterable to list
marks = [45, 67]
new_marks = [79, 84, 92]
marks.extend(new_marks)
print(marks)

vowels = []
vowels.extend('aeiou')
print(vowels)