import sys
input=sys.stdin.readline
n=int(input())
arr=[]
def dfs(arr):
    if len(arr)==n:
        print(*arr)
        return
    for i in range(1,n+1):
        if i not in arr:
            arr.append(i)
            dfs(arr)
            arr.pop()
dfs(arr)