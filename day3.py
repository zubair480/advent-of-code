from string import ascii_lowercase, ascii_uppercase

key = ascii_lowercase + ascii_uppercase
print(key)

with open("input3.txt") as fin:
    data = fin.read().strip()


ans = 0

lines = data.split("\n")
for line in lines:
    n = len(line)
    a = line[:(n//2)]  # First compartment
    b = line[(n//2):]  # Second compartment

    for i, c in enumerate(key):
        if c in a and c in b:
            ans += key.index(c) + 1

print(ans)




ans2 = 0

lines = data.split("\n")
for i in range(0, len(lines), 3):
    a = lines[i:(i + 3)] # The group of three Elves' rucksacks

    for i, c in enumerate(key):
        if all([c in li for li in a]):
            ans2 += key.index(c) + 1

print(ans2)