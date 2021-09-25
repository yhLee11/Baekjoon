from collections import defaultdict
import sys
input=sys.stdin.readline
#비어있는 칸중에 좋아하는 학생이 인접한 칸에 가장 많은 칸
#인접한 칸 중에 비어있는 칸이 가장 많은
#행 번호가 작은칸, 열번호가 작은 칸
dx=[0,0,1,-1]
dy=[1,-1,0,0]
def bfs():
    tuli=[]
    empty=0
    like=0
    for person,people_li in dic.items():
        for i in range(n):
            for j in range(n):
                empty=0
                like=0
                if room[i][j]==0:
                    for k in range(4):
                        nx=dx[k]+i
                        ny=dy[k]+j
                        if 0<=nx<n and 0<=ny<n:
                            if room[nx][ny]==0:
                                empty+=1
                            if room[nx][ny] in people_li:
                                like+=1
                    tuli.append((i,j,empty,like))
        tuli.sort(key=lambda x: (-x[3],-x[2],x[0],x[1]))
        room[tuli[0][0]][tuli[0][1]]=person
        tuli=[]
    # print(room)

def happy():
    happy_point=[0,1,10,100,1000]
    res=0
    for i in range(n):
        for j in range(n):
            li=dic[room[i][j]]
            like=0
            for k in range(4):
                nx=dx[k]+i
                ny=dy[k]+j
                if 0<=nx<n and 0<=ny<n:
                    if room[nx][ny] in li:
                        like+=1
            res+=happy_point[like]
    print(res)

n=int(input().strip())
room=[[0]*n for _ in range(n)]
dic=defaultdict(list)
for i in range(n**2):
    line=list(map(int,input().split()))
    dic[line[0]]+=line[1:]

bfs()
happy()
