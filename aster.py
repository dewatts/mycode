#!/usr/bin/env python3
size=6
for x in range(1,size):
    for y in range(x):
        print("*", end=" ")
    print ("\n")

for z in range(size-2, 0, -1):
    for y in range(z):
        print("*", end=" ")
    print("\n")

