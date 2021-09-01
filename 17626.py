import math
import sys
input=sys.stdin.readline
n=int(input())
dp=[0]*(n+1)
dp[0]=0
dp[1]=1


for i in range(2,n+1):
    if i==(math.sqrt(i))**2:#25
        dp[i]=1#한가지방법
    else:
        dp[i]=i
for i in range(2,n+1):
    for j in range(1,int(math.sqrt(i))+1):
        dp[i]=min(dp[i],dp[j*j]+dp[i-j*j])
        print(dp[i],dp[j*j]+dp[i-j*j])
        print(dp[0:i])
print(dp[n])
