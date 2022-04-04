#구간 합 구하기4
#prefix_sum
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
prefix_sum=[0]
temp=0
for i in num:
    temp+=i
    prefix_sum.append(temp)
# print(prefix_sum)
for i in range(m):
    a,b=map(int,input().split())
    print(prefix_sum[b]-prefix_sum[a-1])
#1 3 = 12
#2 4 = 9
