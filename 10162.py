import sys
input=sys.stdin.readline
T=int(input())
res=[0,0,0]
if T%10!=0:
    print(-1)
else:
    res[0]=T//300
    T=T%300
    res[1]=T//60
    T=T%60
    res[2]=T//10
    print(*res) 
