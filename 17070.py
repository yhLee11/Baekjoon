#1:wall
#1,1 1,2->(1,3),(2,3)가로
#1,2 2,2->(3,2),(3,3)세로
#1,2 2,3->(2,4),(3,3),(3,4)대각선
#가로인 경우: 행이 같음, 세로인 경우: 열이 같음
#대각선인 경우: abs(x2-x1)+abs(y2-y1)=2
#dfs로 모든 경로 구하기
import sys
input=sys.stdin.readline
n=int(input())
map=[list(map(int,input().split())) for _ in range(n)]
start=(0,0)
end=(0,1)
cnt=0
def dfs(start,end):

    if end==(n-1,n-1):
        global cnt
        cnt+=1
        return

    e_right=(end[0],end[1]+1)
    e_diagonal=(end[0]+1,end[1]+1)
    e_bottom=(end[0]+1,end[1])

    if start[0]==end[0]:#가로
        if 0<=e_right[0]<n and 0<=e_right[1]<n:
            if map[e_right[0]][e_right[1]]!=1:
                dfs(end,e_right)
        if 0<=e_right[0]<n and 0<=e_right[1]<n and 0<=e_bottom[0]<n and 0<=e_bottom[1]<n and 0<=e_diagonal[0]<n and 0<=e_diagonal[1]<n:
            if map[e_right[0]][e_right[1]]!=1 and map[e_bottom[0]][e_bottom[1]]!=1 and map[e_diagonal[0]][e_diagonal[1]]!=1:
                dfs(end,e_diagonal)
    elif start[1]==end[1]:#세로
        if 0<=e_bottom[0]<n and 0<=e_bottom[1]<n:
            if map[e_bottom[0]][e_bottom[1]]!=1:
                dfs(end,e_bottom)
        if 0<=e_right[0]<n and 0<=e_right[1]<n and 0<=e_bottom[0]<n and 0<=e_bottom[1]<n and 0<=e_diagonal[0]<n and 0<=e_diagonal[1]<n:
            if map[e_right[0]][e_right[1]]!=1 and map[e_bottom[0]][e_bottom[1]]!=1 and map[e_diagonal[0]][e_diagonal[1]]!=1:
                dfs(end,e_diagonal)
    elif abs(start[0]-end[0])+abs(start[1]-end[1])==2:#대각선
        if 0<=e_right[0]<n and 0<=e_right[1]<n:
            if map[e_right[0]][e_right[1]]!=1:
                dfs(end,e_right)
        if 0<=e_bottom[0]<n and 0<=e_bottom[1]<n:
            if map[e_bottom[0]][e_bottom[1]]!=1:
                dfs(end,e_bottom)
        if 0<=e_right[0]<n and 0<=e_right[1]<n and 0<=e_bottom[0]<n and 0<=e_bottom[1]<n and 0<=e_diagonal[0]<n and 0<=e_diagonal[1]<n:
            if map[e_right[0]][e_right[1]]!=1 and map[e_bottom[0]][e_bottom[1]]!=1 and map[e_diagonal[0]][e_diagonal[1]]!=1:
                dfs(end,e_diagonal)
dfs(start,end)
print(cnt)
