import sys
sys.setrecursionlimit(10000)
input=sys.stdin.readline
r,c=map(int,input().split())
board=[list(map(lambda x:ord(x)-65,input())) for _ in range(r)]
# print(board)
dx=[1,-1,0,0]
dy=[0,0,1,-1]
exist=[0]*26
def dfs(x,y,cnt):
    global count
    print(count,cnt)
    count=max(cnt,count)
    for i in range(4):
        nx=dx[i]+x
        ny=dy[i]+y
        if 0<=nx<r and 0<=ny<c:
            if not exist[board[nx][ny]]:#0이면
                exist[board[nx][ny]]=1
                print(cnt,'dfs',exist)
                dfs(nx,ny,cnt+1)
                exist[board[nx][ny]]=0#backtracking
                print(cnt,'back',exist)
#count로 max 저장해두고 cnt는 백트레킹할 때 쓰이는 변수
count=1
exist[board[0][0]]=1
dfs(0,0,1)
print(count)
