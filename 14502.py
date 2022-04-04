import sys
import copy
from collections import deque
from itertools import combinations
input=sys.stdin.readline
dx=[0,0,1,-1]
dy=[1,-1,0,0]
n,m=map(int,input().split())
board=[list(map(int,input().split())) for _ in range(n)]
ans=-sys.maxsize
def spread_virus_bfs(virus_list):
	q=deque()
	q.extend(virus_list)
	while q:
		x,y=q.popleft()
		visit[x][y]=1
		for i in range(4):
			nx=dx[i]+x
			ny=dy[i]+y
			if 0<=nx<n and 0<=ny<m and new_board[nx][ny]==0 and visit[nx][ny]==0:
				visit[nx][ny]=1
				new_board[nx][ny]=2
				q.append((nx,ny))
	zero_cnt=0
	for i in range(n):
		for j in range(m):
			if new_board[i][j]==0:
				zero_cnt+=1
	global ans
	ans=max(zero_cnt,ans)

coordinates=[]
virus_list=[]
for i in range(n):
	for j in range(m):
		if board[i][j]==0:
			coordinates.append((i,j))
		if board[i][j]==2:
			virus_list.append((i,j))
wall = list(combinations(coordinates,3))	

for a,b,c in wall:
	new_board=copy.deepcopy(board)
	new_board[a[0]][a[1]]=1
	new_board[b[0]][b[1]]=1
	new_board[c[0]][c[1]]=1
	visit=copy.deepcopy(new_board)
	for i in range(n):
		for j in range(m):
			if new_board[i][j]==2:
				spread_virus_bfs(virus_list)
print(ans)