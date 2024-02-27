#!/usr/bin/python3
for letter in range(90, 64, -1):
    if letter % 2 == 0:
        i = 32
    else:
        i = 0
    print("{}".format(chr(letter+i)), end="")
