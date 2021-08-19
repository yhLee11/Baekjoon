import heapq
import sys
input=sys.stdin.readline
n=int(input())
h=[]
for i in range(n):
    x=int(input())
    if x==0:
        if h:
            print(heapq.heappop(h))
        else:
            print(0)
    else:
        heapq.heappush(h,x)
