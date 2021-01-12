#!/usr/bin/python3

import itertools
import sys
from itertools import product

import tqdm

print("Please input the minimum len :")
mimin = input()
try:
    mimin = int(mimin)
except Exception as e:
    print(e)
    sys.exit("There is a problem with min please enter a number !\n")
print("\n")

if mimin <= 0:
    sys.exit("min must be greater than 0\n")

print("If you want a unique len, please input the same maximum len as minimum"
      "len. \n")

print("Please input the maximum len :")
mamax = input()
try:
    mamax = int(mamax) + 1
except Exception as e:
    print(e)
    sys.exit("There is a problem with max please enter a number !\n")
print("\n")

if mimin >= mamax:
    sys.exit("min must be less than max\n")

print("Please input the alphabet :")
alphabet = input()
print("\n")

# Let's remove duplicate char
ch = "".join(set(alphabet))

print("Please input the name of the output file :")
name = input()

with open(name, 'w+', errors='ignore') as f:
    for w in range(mimin, mamax):
        print("\nBegin for len =", w, "\n")
        print("There is ", len(ch)**w, "chains.\n")
        for u in tqdm.tqdm(product(ch, repeat=w)):
            chain = ''.join(u)
            f.write(chain + "\n")
print("\nClosing file...\n")
f.close()
print("Exiting...\n")