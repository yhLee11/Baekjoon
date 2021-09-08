"""https://pacific-ocean.tistory.com/388"""
from collections import deque
import sys
input=sys.stdin.readline
t=int(input())

def bfs():
    q=deque()
    q.append([a,''])
    while q:
        num,res=q.popleft()
        dn=(num*2)%10000
        if dn==b: return res+"D"
        elif visit[dn]==0:
            visit[dn]=1
            q.append([dn,res+"D"])

        sn=num-1 if num!=0 else 9999
        if sn==b:return res+"S"
        elif visit[sn]==0:
            visit[sn]=1
            q.append([sn,res+"S"])

        ln=int(num%1000*10+num/1000)#234*10 + 1
        if ln==b:return res+"L"
        elif visit[ln]==0:
            visit[ln]=1
            q.append([ln,res+"L"])

        rn=int(num%10*1000+num//10)
        if rn==b:return res+"R"
        elif visit[rn]==0:
            visit[rn]=1
            q.append([rn,res+"R"])

for _ in range(t):
    a,b=map(int,input().split())
    visit=[0 for _ in range(10000)]
    print(bfs())
