import sys
input=sys.stdin.readline
n=int(input())
chess=[0 for _ in range(n)]
cnt=0

def check(start):
    #1)같은열 2)대각선
    for i in range(start):
        if chess[start]==chess[i] or start-i == abs(chess[start]-chess[i]):
            return False
    return True

def dfs(start):#행
    if start==n:
        global cnt
        cnt+=1
        return 

    for i in range(n):
        chess[start]=i
        if check(start):
            dfs(start+1)

dfs(0)
print(cnt)