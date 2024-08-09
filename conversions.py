#conversions

# string to int
string = "123"
number = int(string)
print(number * number)
# int to string
num = 123
string2 = str(num)
#binary, octal, hexa decimal to decimal
binary_string = "10111"
octal_string = "123"
hex_string = "AA"
print(int(binary_string, 2))
print(int(octal_string, 8))
print(int(hex_string, 16))
# to binary, octal, hexa decimal
n1 = 23
n2 = 83
n3 = 170
print(bin(n1))
print(bin(n2))
print(hex(n3))