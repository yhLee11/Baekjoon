import sys
input=sys.stdin.readline
T=int(input().strip())


for i in range(T):
    k=int(input().strip())
    dp=[1,1,1]
    for i in range(k-3):
        total=dp[i]+dp[i+1]
        dp.append(total)
    print(dp[-1])
