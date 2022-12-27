# with open("input6.txt") as fin:
#     data = fin.read().strip()

# i = 0
# while True:
#     s = data[i:(i+4)]
#     if len(set(list(s))) == 4:
#         print(i + 4)
#         break

#     i += 1


with open("input6.txt") as fin:
    data = fin.read().strip()

i = 0
while True:
    s = data[i:(i+14)]
    if len(set(list(s))) == 14:
        print(i + 14)
        break

    i += 1