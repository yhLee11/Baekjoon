import sys
input=sys.stdin.readline
n,k=map(int,input().split())
knapsack=[[0]*(k+1) for _ in range(n+1)]
wv=[[0,0]]
for _ in range(n):
    wv.append(list(map(int,input().split())))

for i in range(1,n+1):
    weight=wv[i][0]
    value=wv[i][1]
    # print('weight ',weight,' value ',value)
    for j in range(1,k+1):
        if j<weight:
            # print('if knap[i][j]',i,j,knapsack[i][j])
            knapsack[i][j]=knapsack[i-1][j]
        else:
            # print('else knap[i][j]',i,j,knapsack[i][j],knapsack[i-1][j-weight]+value,knapsack[i-1][j])
            knapsack[i][j]=max(knapsack[i-1][j-weight]+value,knapsack[i-1][j])
print(knapsack[n][k])
            
