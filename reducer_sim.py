#!/usr/bin/python
import sys
import math
precision_num = 4
single_dict = {}
single_file = open("single.txt")
for line in single_file:
    key,num = line.strip().split()
    single_dict[key] = int(num)

for line in sys.stdin:
    pair, value = line.strip().split()
    keyA, keyB = pair.split("&")
    fenZi = int(value)
    #fenMu = single_dict[keyA] + single_dict[keyB] - fenZi
    fenMu = round(math.sqrt(single_dict[keyA] * single_dict[keyB]), precision_num)
    sim = round(float(fenZi)/fenMu, precision_num)
    if sim != 0 and fenZi > 1 and fenMu > 2:
        print " ".join([keyA, keyB, str(sim), str(fenZi), str(fenMu)])
        print " ".join([keyB, keyA, str(sim), str(fenZi), str(fenMu)])
