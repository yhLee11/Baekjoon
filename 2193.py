import sys
input=sys.stdin.readline
N=int(input())
dp=[[0 for _ in range(2)] for _ in range(91)]
dp[1][1]=1
dp[2][0]=1
for i in range(3,91):
    for j in range(2):
        if j==0:
            dp[i][j]=dp[i-1][0]+dp[i-2][0]
        else:
            dp[i][j]=dp[i-1][1]+dp[i-2][1]
print(sum(dp[N]))
