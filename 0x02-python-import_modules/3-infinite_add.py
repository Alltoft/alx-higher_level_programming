#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    l = len(argv)
    i = 1
    a = 0
    while i < l:
        a += int(argv[i])
        i += 1
    if l == 0:
        print(0)
    else:
        print(a)
