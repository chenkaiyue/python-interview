import heapq
import random

test_list=[]
for i in range(10000):
    test_list.append(random.random()*1000000)
print heapq.nlargest(10,test_list)
print heapq.nsmallest(10,test_list)