"""  # 1.30

def unicode_multiplication(s, num):
    max_ = max(s)
    return ord(max_) * num
ans = unicode_multiplication('Baba', 7)
print(ans)

# 1.29

def is_reverse(num1, num2):
    if str(num1) == str(num2)[::-1]:
        return True
    return False
print(is_reverse(123, 327))

# 1.28

def is_lucky(num):
    if str(num) == str(num)[::-1]:
        return True
    return False
print(is_lucky(179))

# 1.27

def digit_count(num, digit):
    count = str(num).count(str(digit))
    return count
print(digit_count(7777777, 7))

# 1.26

def is_present(num, digit):
    cnt = str(num).count(str(digit))
    if cnt >= 1:
        return True
    return False
print(is_present(777, 9))  

# random
import random
ages = []
for i in range(10):
    ages.append(random.randint(1, 100))
child = []
adult = []
old = []
for i in ages:
    if i <= 15:
        child.append(i)
    elif i > 15 and i < 50:
        adult.append(i)
    else :
        old.append(i)
print(ages)
print(child, adult, old, sep='\n')   

# list comprehension
names = ['walter', 'jesse0', 'skylerr', 'saul']
new_names = [each_name for each_name in names if each_name[0] == 's']   
print(new_names)   

import math
x = [9, 16, 25]
new_list = [math.sqrt(each_num) for each_num in x]
print(new_list)

# cube list comprehension
def cube(x):
    return x * x * x
nums = [10, 20, 30]
new_list = [cube(i) for i in nums]
print(new_list)

# printing a to z
chars = [chr(i) for i in range(97, 123)]                # chr(i) - converts int to char
print(chars)

# printing factors
n = 10
factors = [i for i in range(1, n+1) if n % i == 0]
print(factors)

# is_prime'
def is_prime(n):
    return len([i for i in range(1, n+1) if n % i == 0]) == 2
primes = [1 for i in range(1, 101) if is_prime(i)]
print(primes)    """

numbers = [number for number in range(10, 100) if abs(number//10 - number%10) == 1]
print(numbers)