#!/usr/bin/python
import sys
import heapq
recommend_num = 400
old_keyA = ""
old_recommend_list = []

for line in sys.stdin:
    keyA, keyB, value, fenZi, fenMu = line.strip().split()
    sim = float(value)
    if keyA == old_keyA:
        if len(old_recommend_list) < recommend_num:
            heapq.heappush(old_recommend_list, (sim, keyB, fenZi, fenMu))
        else:
            if old_recommend_list[0][0] < sim:
                heapq.heappushpop(old_recommend_list, (sim, keyB, fenZi, fenMu))
    else:
        if old_keyA != "":
            old_recommend_list.reverse()
            print old_keyA + " "+" ".join([str(x[1])+","+str(x[0])+","+str(x[2])+","+str(x[3]) for x in old_recommend_list])
        old_keyA = keyA
        old_recommend_list = [(sim, keyB, fenZi, fenMu)]
old_recommend_list.reverse()
print old_keyA + " " + " ".join([str(x[1])+","+str(x[0])+","+str(x[2])+","+str(x[3]) for x in old_recommend_list])