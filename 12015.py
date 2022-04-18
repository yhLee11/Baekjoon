import sys
input=sys.stdin.readline
n=int(input())
A=list(map(int,input().split()))
LIS=[0]
for a in A:
    if a>LIS[-1]:
        LIS.append(a)
    else:
        left=0
        right=len(LIS)
        while left<right:
            mid=(left+right)//2
            if LIS[mid]<a:
                left=mid+1
            else:#LIS[mid]>=a
                right=mid
        #     print(left,mid,right)
        # print(LIS)
        LIS[right]=a

print(len(LIS)-1)