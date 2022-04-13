import sys
input=sys.stdin.readline
v=int(input())
tree=[[0]*v for _ in range(v)]
maxlen=-sys.maxsize
stk=[]
visit=[False for _ in range(v)]
cnt=0
#1 - 3
#2 - 4
#3 - 1 4
#4 - 2 3 5
#5 - 4
def dfs(s):
    stk=[]
    stk.append(tree[s].reverse())
    visit=[False for _ in range(v)]
    while stk:
        node

# print(tree)
for i in range(v):
    n=list(map(int,input().split()))
    start=n[0]
    for j in range(1,len(n)-1,2):
        tree[start-1][n[j]-1]=n[j+1]
# print(tree)

