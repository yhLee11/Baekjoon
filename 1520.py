import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
dx=[1,-1,0,0]
dy=[0,0,1,-1]

def dfs(x,y):
    if x==h-1 and y==w-1:
        return 1
    if dp[x][y]==-1:
        dp[x][y]=0
        for i in range(4):
            nx=x+dx[i]
            ny=y+dy[i]
            if 0<=nx<h and 0<=ny<w:
                if maps[nx][ny]<maps[x][y]:
                    dp[x][y]+=dfs(nx,ny)
    print(dp)
    return dp[x][y]
h,w=map(int,input().split())
maps=[list(map(int,input().split())) for _ in range(h)]
dp=[[-1 for _ in range(w)] for _ in range(h)]

print(dfs(0,0))

#dp
#0이면 목적지까지 갈 수 있는 경로가 없으므로 0반환
#1이상의 값이면 이전에 연산한 방문 경로가 있으므로 해당 값을 반환해서 더해줌
#-1이면 방문하지 않은 경로이므로 정상적으로 DFS+DP 실행
