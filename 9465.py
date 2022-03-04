import sys
input=sys.stdin.readline
t=int(input())
for _ in range(t):
    n=int(input())
    stk0=list(map(int,input().split()))
    stk1=list(map(int,input().split()))
    for i in range(1,n):
        if i==1:
            stk0[i]+=stk1[i-1]
            stk1[i]+=stk0[i-1]
        else:
            stk0[i]+=max(stk1[i-1],stk1[i-2])
            stk1[i]+=max(stk0[i-1],stk0[i-2])
    print(max(stk0[-1],stk1[-1]))