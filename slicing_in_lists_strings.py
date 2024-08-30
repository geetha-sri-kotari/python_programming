# slicing in lists / strings
# process of getting sub-lists/ sub-strings from list or string
# returns new-list or new string
# done using indexes
# list_name[::],, list_name[:]
# list_name[start: stop: step]
# stop_index is excluded
# defaults - start: 0, stop: len(list), step: 1

x = [10, 20, 30, 40, 50]
slice1 = x[1::]          # start = 1, stop = len(list), step = 1
print(slice1)
slice2 = x[::]           # start = 0
print(slice2)
slice3 = x[1:4:2]        # start = 1, stop = 4-1, step = 2
print(slice3)
# one colon - step is one by default
print(x[:])
# slice in reverse order
print(x[-1:-4:-1])