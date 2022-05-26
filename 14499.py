import sys
from collections import deque
input=sys.stdin.readline
n,m,x,y,k=map(int,input().split())
s=[list(map(int,input().split())) for _ in range(n)]
move=list(map(int,input().split()))
dice=[0]*6
def turn(num):
    global dice
    if num==1:#동
        dice=[dice[2],dice[1],dice[5],dice[0],dice[4],dice[3]]
    elif num==2:
        dice=[dice[3],dice[1],dice[0],dice[5],dice[4],dice[2]]
    elif num==3:
        dice=[dice[4],dice[0],dice[2],dice[3],dice[5],dice[1]]
    elif num==4:
        dice=[dice[1],dice[5],dice[2],dice[3],dice[0],dice[4]]
dic={1:(0,1),2:(0,-1),3:(-1,0),4:(1,0)}
for i in move:
    mx,my=dic[i]
    x+=mx
    y+=my
    if 0<=x<n and 0<=y<m:
        turn(i)
        if s[x][y]==0:
            s[x][y]=dice[5]
        else:
            dice[5]=s[x][y]
            s[x][y]=0
        print(dice[0])
    else:
        x-=mx
        y-=my