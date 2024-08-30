# def keyword to create your own functions
# not need to mention return type

def print_hello():
    print("hello")

def add_two(a, b):
    return a + b

print_hello()
ans = add_two(10, 20)
print(ans)

# Functions :
# function with return value and with argument
# without return value and with arguments
# with retrn value and without arguments
# without return value and without arguments

max_of_3 = max(10, 20, 30)
print(max_of_3)

# void function
def location(city, country, continent):
    print(f"{city} is in {country}, which is in {continent}")
location('Hyderabad', 'India', 'Asia')         # positional arguments
location(continent='Asia', country='India', city='Mumbai')      # keyword arguments
# no positional argument should follow a keyword argument
# after keyword arguments no positional arguments should be passed

# default values to parameters in Python
def location(city, country, continent="Asia"):
    print(f"{city} is in {country}, which is in {continent}")
location('Berlin', 'Germany', 'Europe')      # if 3rd value is passed default value is ignored

a = "123"
print(int(a, 8))      # 123 base = 10

x = [10, 20, 30]
print(sum(x))
print(sum(x, 100))       # by default second argument is zero

# input function

def getInt():
    a = int(input("Enter a number: "))
    return a
b = getInt()
print(2 * b)