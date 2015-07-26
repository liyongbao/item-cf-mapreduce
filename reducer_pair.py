#!/usr/bin/python
import sys

old_pair = ""
old_num = 0

for line in sys.stdin:
    pair,value = line.strip().split()
    if pair == old_pair:
        old_num += int(value)
    else:
        if old_pair != "":
            print old_pair + "\t" + str(old_num)
        old_pair = pair
        old_num = int(value)
print old_pair + "\t" + str(old_num)
