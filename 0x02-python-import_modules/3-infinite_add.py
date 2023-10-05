#!/usr/bin/python3
if __name__ == "__main__":
    from sys import argv
    n = len(argv)
    i = 1
    a = 0
    while i < n:
        a += int(argv[i])
        i += 1
    print(a)
