# pangram -> string in which you can find all alphabets

import string
print(string.ascii_lowercase)

# lowe method
# s = input().lower() -> takes uppercase as lowercase

s ="a quick brown fox jumps over the lazy dog"
x = set(s)
x.discard(' ')
if len(x) == 26:
    print("Pangram")
else :
    print("Not Pangram")