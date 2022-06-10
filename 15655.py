import sys
input=sys.stdin.readline
n,m=map(int,input().split())
arr=list(map(int,input().split()))
arr.sort()
s=[]
def dfs(depth):
    if len(s)==m:
        print(' '.join(map(str,s)))
        return 
    for i in range(n):
        if depth==0 or s[depth-1]<arr[i]:
            s.append(arr[i])
            dfs(depth+1)
            s.pop()

dfs(0)
