import sys
from collections import deque
input=sys.stdin.readline
k=int(input())
sum=0
dq=deque()
for i in range(k):
    num=int(input())
    if num:
        dq.append(num)
        sum+=num
    else:
        sum-=dq.pop()
print(sum)
