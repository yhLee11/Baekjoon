import sys
from collections import deque
input=sys.stdin.readline
n=int(input())
graph=[[0]*n for _ in range(n)]
k=int(input())
for _ in range(k):
    a,b=map(int,input().split())
    graph[a-1][b-1]=2#apple
L=int(input())
dic=dict()
for _ in range(L):
    num,direct=input().split()
    dic[int(num)]=direct

dx=[0,1,0,-1]#오른쪽,아래,왼쪽,위
dy=[1,0,-1,0]
cnt=0
dr=0
def turn(strdr):
    global dr
    if strdr=='L':
        dr=(dr-1)%4
    else:
        dr=(dr+1)%4    
def sol(x,y):
    global cnt,dr
    q=deque()
    q.append((x,y))
    graph[x][y]=1
    while True:
        cnt+=1
        x=dx[dr]+x
        y=dy[dr]+y
        if 0<=x<n and 0<=y<n:
            if graph[x][y]==2:
                graph[x][y]=1
                q.append((x,y))
                if cnt in dic:
                    turn(dic[cnt])
            elif graph[x][y]==0:
                graph[x][y]=1
                q.append((x,y))
                tx,ty=q.popleft()
                graph[tx][ty]=0
                if cnt in dic:
                    turn(dic[cnt])
            else:
                break
        else:break

sol(0,0)
print(cnt)