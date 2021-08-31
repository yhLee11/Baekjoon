import sys
input=sys.stdin.readline
n=int(input())
lst=[list(map(int,input().split())) for _ in range(n)]
res=[0,0,0]
def cut(x,y,n):
    num=lst[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if num!=lst[i][j]:
                cut(x,y,n//3)
                cut(x,y+n//3,n//3)
                cut(x,y+n//3*2,n//3)

                cut(x+n//3,y,n//3)
                cut(x+n//3,y+n//3,n//3)
                cut(x+n//3,y+n//3*2,n//3)

                cut(x+n//3*2,y,n//3)
                cut(x+n//3*2,y+n//3,n//3)
                cut(x+n//3*2,y+n//3*2,n//3)

                return

    if num==-1:
        res[0]+=1
    elif num==0:
        res[1]+=1
    else:
        res[2]+=1

cut(0,0,n)
for i in res:print(i)
