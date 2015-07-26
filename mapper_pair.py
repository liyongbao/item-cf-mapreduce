#!/usr/bin/python
# coding=utf-8
import sys
import itertools
temp_dict = {}
max_len = 1000000  # 没有使用Combiner,可以在map中自己实现一个。temp_dict就是这个目的
for line in sys.stdin:
    sp = line.strip().split()
    item_list = sp[1:]
    if len(item_list) < 2:
        continue
    for item_pair in itertools.combinations(item_list, 2):
        if item_pair[0] < item_pair[1]:
            pair = "&".join([item_pair[0], item_pair[1]])
        else:
            pair = "&".join([item_pair[1], item_pair[0]])
        if pair in temp_dict:
            temp_dict[pair] += 1
        else:
            if len(temp_dict) > max_len:
                for key, value in temp_dict.iteritems():
                    print " ".join([key, str(value)])
                temp_dict.clear()
            temp_dict[pair] = 1

for key, value in temp_dict.iteritems():
    print " ".join([key, str(value)])



