#swapping numbers
a, b = 10, 20
a, b = b, a
print(a, b)
#separate in new lines
age, name, cgpa = 18, "surekha", 9.1
print(age, name, cgpa, sep='\n')
#Truthiness of values in python
#bool() function is built_in function can be used to check the truthiness of a value
print(bool(0))
print(bool(-1))
print(bool(0.0))
print(bool(0.1))
print(bool())
print(bool("")) #false
print(bool(",")) #true
print(bool([])) #false
print(bool([0])) #true
#any() , all()
#any() - takes a collection and will return true if at least one item is true
#all() - takes a collection and will return true if all of the items are true
list_of_boolean_values = [0, 0.0, [1], ""]
print(any(list_of_boolean_values))
print(all(list_of_boolean_values))
