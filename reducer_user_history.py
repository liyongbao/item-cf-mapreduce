#!/usr/bin/python
# coding=utf-8
import sys
old_key = ""
old_set = set()
for line in sys.stdin:
    key, value = line.strip().split()
    if key == old_key:
        old_set.add(value)
    else:
        if old_key != "":
            print old_key+" "+" ".join(old_set)
        old_key = key
        old_set = set()
        old_set.add(value)
print old_key + " " + " ".join(old_set)
