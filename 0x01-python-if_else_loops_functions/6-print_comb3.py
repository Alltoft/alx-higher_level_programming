#!/usr/bin/python3
for i in range(0, 10):
    if i == 8:
        break
    for a in range(i, 10):
        if a == i:
            continue
        print('{}{}'.format(i, a), end=", ")
print('{}{}'.format(i, a))
