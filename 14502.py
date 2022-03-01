from collections import deque
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
dx=[1,-1,0,0]
dy=[0,0,1,-1]

board=[list(map(int,input().split())) for _ in range(n)]
