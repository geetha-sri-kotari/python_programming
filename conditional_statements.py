#conditional statemnts in python
a = 10
b = 20
c = 30
if a > b and a > c:
    print(a)
elif b > a and b > c:
    print(b)
else:
    print(c)
# single line if else(kind of ternary)
n = int(input("enter a number: "))
print("Even" if n % 2 == 0 else "Odd")