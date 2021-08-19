import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
num=sorted(num)

stk=[]
def dfs(stk):
    if len(stk)==m:
        print(' '.join(map(str,stk)))
    for i in num:
        if i in stk:
            continue
        dfs(stk+[i])

dfs(stk)
