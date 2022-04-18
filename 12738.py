import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
LIS=[-1000000001]
for a in A:
    if a>LIS[-1]:
       LIS.append(a)
    else:
        left,right=0,len(LIS)
        while left<right:
            mid=(left+right)//2
            if LIS[mid]<a:
                left=mid+1
            else:
                right=mid
        LIS[right]=a

print(len(LIS)-1)
