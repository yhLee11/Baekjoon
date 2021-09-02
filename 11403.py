import sys
input=sys.stdin.readline
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]

for k in range(n):
    for i in range(n):
        for j in range(n):
            if lst[i][j]==1 or (lst[i][k]==1 and lst[k][j]==1):
                lst[i][j]=1
            else:
                lst[i][j]=0

for i in lst:
    print(' '.join(map(str,i)))
