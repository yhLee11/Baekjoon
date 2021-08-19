import sys
input=sys.stdin.readline
t=int(input())

for i in range(t):
    h,w,n=map(int,input().split())#호텔층수, 각층방수, 몇번째손님
    quo=n//h+1
    mod=n%h
    if mod==0:
        mod=h
        quo-=1
    print(mod*100+quo)
