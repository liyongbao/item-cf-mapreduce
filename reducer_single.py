#!/usr/bin/python
import sys
old_item = ""
old_num = 0
for line in sys.stdin:
    item, count = line.strip().split()
    if item == old_item:
        old_num += int(count)
    else:
        if old_item != "":
            print old_item + " " + str(old_num)
        old_item = item
        old_num = int(count)
print old_item + " " + str(old_num)
