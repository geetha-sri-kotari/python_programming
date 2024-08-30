students = [["23A91A0519", "surekha", 18], ["23A91A0529", "geetha", 18], ["23A91A0534", "krish", 20]]
for each_student in students :
    for each_record in each_student :
        print(each_record, end = ' ')
    print()

# special looping technique
# only when lengths of inner iterables is fix( same )
for roll, name, age in students :
    print(roll, name, age)

d = {'sachin' : 100, 'kohli' : 80, 'ponting' : 77}
print(d.items())
for k, v in d.items():
    print(k, v)