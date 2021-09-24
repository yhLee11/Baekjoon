from collections import defaultdict
from collections import deque
import sys
input=sys.stdin.readline
#비어있는 칸중에 좋아하는 학생이 인접한 칸에 가장 많은 칸
#인접한 칸 중에 비어있는 칸이 가장 많은
#행 번호가 작은칸, 열번호가 작은 칸
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def first(x,y):
    favorite=0
    for i in range(4):
        nx=x+dx[i]#행
        ny=y+dy[i]#열
        if 0<=nx<n and 0<=ny<n:
            if room[nx][ny] in dic[room[nx][ny]]:#좋아하는 사람
                favorite+=1
    return favorite
def second(x,y):
    empty=0
    for i in range(4):
        nx=x+dx[i]#행
        ny=y+dy[i]#열
        if 0<=nx<n and 0<=ny<n:
            if room[nx][ny]==0:#빈자리
                empty+=1
    return empty


n=int(input().strip())
room=[[0]*n for _ in range(n)]
dic=defaultdict(list)
order=[]
for i in range(n**2):
    temp=list(map(int,input().split()))
    dic[temp[0]]+=temp[1:]
    order.append(temp[0])

for st in order:
    fv=defaultdict(list)
    for i in range(n):
        for j in range(n):
            if room[i][j]==0:
                fv[first(i,j)].append((i,j))#좋아하는 사람 key=좋아하는사람수 value=자리
    s=dic[st]
    s=sorted(fv.items(),key=lambda x: -x[0])#많은순
    print(s)
    if len(fv[s[0][0]])>1:
        dic2=defaultdict(list)
        for i,j in fv[s[0][0]]:
            dic2[second(i,j)].append((i,j))
        s=sorted(dic2.items(),key=lambda x:-x[0])
        room[dic2[s[0][0]][0][0]][dic2[s[0][0]][0][1]]=st
    else:
        room[fv[s[0][0]][0][0]][fv[s[0][0]][0][1]]=st
print(room)
