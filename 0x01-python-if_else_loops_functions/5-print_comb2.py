#!/usr/bin/python3
for a in range(100):
    print("{:0>2}".format(a), end=", " if a < 99 else "\n")
