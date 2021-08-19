import sys
input=sys.stdin.readline
a,b=map(int,input().split())

L,R=0,0

while True:
    if a>b:
        L+=1
        a-=b
    elif a<b:
        R+=1
        b-=a
    else:
        print(L,R)
        break
