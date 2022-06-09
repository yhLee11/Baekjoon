import sys
input=sys.stdin.readline
def dfs(start,depth):
    if depth==6:
        print(' '.join(map(str,combi)))
        return
    for i in range(start,len(s)):
        combi[depth]=s[i]
        dfs(i+1,depth+1)

k=-1
combi=[0 for i in range(6)]
while k!=0:
    lst=list(map(int,input().split()))
    k=lst[0]
    s=lst[1:]
    dfs(0,0)
    print()