import sys
input=sys.stdin.readline
n=int(input())
arr=list(map(int,input().split()))
ans=-sys.maxsize
s=[]
visit=[False]*n
def dfs(s):
    global ans
    if len(s)==n:
        hap=0
        for i in range(n-1):
            hap+=abs(s[i]-s[i+1])
        ans=max(ans,hap)    
        return
    for i in range(n):
        if not visit[i]:
            s.append(arr[i])
            visit[i]=True
            dfs(s)
            s.pop()
            visit[i]=False

dfs(s)
print(ans)