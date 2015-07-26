#!/usr/bin/python
# coding=utf-8
import sys
max_len = 1000000  # 没有使用Combiner,可以在map中自己实现一个。temp_dict就是这个目的
temp_dict = {}
for line in sys.stdin:
    sp = line.strip().split()
    user_id = sp[0]
    item_list = sp[1:]
    if len(item_list) < 2:
        continue
    for item in item_list:
        if item in temp_dict:
            temp_dict[item] += 1
        else:
            if len(temp_dict) > max_len:
                for key, value in temp_dict.iteritems():
                    print key, value
                temp_dict.clear()
            temp_dict[item] = 1
for key, value in temp_dict.iteritems():
    print key, value