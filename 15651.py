import sys
input=sys.stdin.readline
n,m=map(int,input().split())
stk=[]

def dfs(stk):
    if len(stk)==m:
        print(' '.join(map(str,stk)))
        return
    for i in range(1,n+1):
        dfs(stk+[i])

dfs(stk)
