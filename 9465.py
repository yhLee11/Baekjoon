import sys
input=sys.stdin.readline
t=int(input())
ans=[]
for _ in range(t):
    n=int(input())
    stk0=list(map(int,input().split()))
    stk1=list(map(int,input().split()))
    if n==1:
        print(max(stk0[0],stk1[0]))
        continue
    elif n==2:
        sum1=stk0[0]+stk1[1]
        sum2=stk1[0]+stk0[1]
        print(max(sum1,sum2))
        continue

    sum_max=0
    dp=[]
    sum1=stk0[0]+stk1[1]
    sum2=stk1[0]+stk0[1]
    if sum1>sum2:
        dp=[0,1]
        sum_max=sum1
    else:
        dp=[1,0]
        sum_max=sum2

    for i in range(1,n-1):
        if dp[i-1]==0:
            sum1=stk0[i-1]+stk1[i]+stk0[i+1]
            sum2=stk0[i-1]+stk1[i+1]
            if sum1>sum2:
                dp.append(0)
                sum_max+=stk0[i+1]
            else:
                dp[-1]=-1
                dp.append(1)
                sum_max-=stk1[i]
                sum_max+=stk1[i+1]
        elif dp[i-1]==1:
            sum1=stk1[i-1]+stk0[i]+stk1[i+1]
            sum2=stk1[i-1]+stk0[i+1]
            if sum1>sum2:
                dp.append(1)
                sum_max+=stk1[i+1]
            else:
                dp[-1]=-1
                dp.append(0)
                sum_max-=stk0[i]
                sum_max+=stk0[i+1]

        elif dp[i-1]==-1:
            two1=stk1[i]+stk0[i+1]
            two0=stk0[i]+stk1[i+1]
            if dp[i]==0:sum_max-=stk0[i]
            else:sum_max-=stk1[i]
            if dp[i-2]==0:
                sum3=stk1[i-1]+stk0[i]+stk1[i+1]
                sum2=stk1[i-1]+stk0[i+1]
                max_num=max(sum3,sum2,two1,two0)
                if max_num==sum3:#sum3>sum2:
                    dp[i-1]=1
                    dp[i]=0
                    dp.append(1)
                    sum_max+=sum3
                elif max_num==sum2:
                    dp[i-1]=1
                    dp[i]=-1
                    dp.append(0)
                    sum_max+=sum2
                elif max_num==two1:
                    dp[i]=1
                    dp.append(0)
                    sum_max+=two1
                else:
                    dp[i]=0
                    dp.append(1)
                    sum_max+=two0
            elif dp[i-2]==1:
                sum3=stk0[i-1]+stk1[i]+stk0[i+1]
                sum2=stk0[i-1]+stk1[i+1]
                max_num=max(sum3,sum2,two0,two1)
                if max_num==sum3:#sum3>sum2:
                    dp[i-1]=0
                    dp[i]=1
                    dp.append(0)
                    sum_max+=sum3
                elif max_num==sum2:
                    dp[i-1]=0
                    dp[i]=-1
                    dp.append(1)
                    sum_max+=sum2
                elif max_num==two1:
                    dp[i]=1
                    dp.append(0)
                    sum_max+=two1
                else:
                    dp[i]=0
                    dp.append(1)
                    sum_max+=two0
    ans.append(sum_max)
for a in ans:
    print(a)