import sys
input=sys.stdin.readline
n=int(input())
chV=list(map(int,input().split()))
chV.sort()
ans=sys.maxsize
#-99 -2 -1 4 98
left,right=0,n-1
res=[]
while left<right:
    num=chV[left]+chV[right]
    if abs(num)<ans:
        ans=abs(num)
        res=[chV[left],chV[right]]
    if num<0:
        left+=1
    else:
        right-=1

print(res[0],res[1])
