from collections import deque
import sys
input=sys.stdin.readline
n,k=map(int,input().split())
lst=[i+1 for i in range(n)]
dq=deque(lst)
print('<',end='')
while True:
    if len(dq)==1:
        print(dq.popleft(),end='>')

        break

    for i in range(k-1):
        dq.append(dq.popleft())

    print(dq.popleft(), end=', ')


"""
dq=3 6 2 7 5 1 4
1' 2 3 4 5 6 7
1 2 4' 5 6 7
1 2 4 5 7'
1 4' 5 7
...


"""
