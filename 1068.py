import sys
def dfs(n,arr):
    arr[n]=-2
    for i in range(len(arr)):
        if n==arr[i]:
            dfs(i,arr)

num=int(sys.stdin.readline())
arr=list(map(int,sys.stdin.readline().split()))
k=int(sys.stdin.readline())
dfs(k,arr)
cnt=0
for i in range(len(arr)):
    if arr[i]!=-2 and i not in arr:#-2가 아니면서 다른 노드의 부모가 아닌 원소
        cnt+=1
print(cnt)
