batsmen = ["sachin", "kohli", "ponting"]
centuries = [100, 80, 77]
d = {batsmen[i]:centuries[i] for i in range(len(batsmen))}
print(d)

# {'a' : 1, 'b' : 2 ....'z' : 26}
ch = 97
d = {}
for i in range(1, 27):
    key = chr(ch)
    d[key] = i
    ch = ch + 1
print(d)

# using comprehension
d = {chr(i + 96): i for i in range(1, 27)}
print(d)