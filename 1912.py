import sys
input=sys.stdin.readline
n=int(input())
num=list(map(int,input().split()))
dp=[0]*len(num)
dp[0]=num[0]
for i in range(1,len(num)):
    dp[i]=max(dp[i-1]+num[i],num[i])
print(max(dp))