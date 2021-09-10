from collections import deque
import sys
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def bfs(i,j):
    q=deque()
    q.append((i,j))
    
