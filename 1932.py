import sys
sys=sys.stdin.readline
n=int(input())
num=[]
for _ in range(n):
    num.append(list(map(int,input().split())))
idx=1
for i in range(1,n):
    num[i][0]+=num[i-1][0]
    for j in range(1,idx):
        num[i][j]+=max(num[i-1][j-1],num[i-1][j])
    num[i][-1]+=num[i-1][-1]
    idx+=1
print(max(num[-1]))
