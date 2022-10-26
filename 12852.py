import sys
input=sys.stdin.readline
from collections import deque
N=int(input())

def bfs(start):
    q=deque()
    q.append([start])
    while q:
        lst=q.popleft()
        x=lst[0]
        if x==1:
            print(len(lst)-1)
            print(*lst[::-1])
            break
        if x%3==0:
            q.append([x//3]+lst)
        if x%2==0:
            q.append([x//2]+lst)
        
        q.append([x-1]+lst)      
bfs(N)