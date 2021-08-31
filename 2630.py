import sys
input=sys.stdin.readline
n=int(input())
paper=[list(map(int,input().split())) for _ in range(n)]
blue,white=0,0
def rec(x,y,n):
    global blue, white
    check=paper[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if check!=paper[i][j]:
                rec(x,y,n//2)#1사분면
                rec(x,y+n//2,n//2)#2사분면
                rec(x+n//2,y,n//2)#3사분면
                rec(x+n//2,y+n//2,n//2)#4사분면
                return
    if check==1:
        blue+=1
    else:
        white+=1
rec(0,0,n)
print(white)
print(blue)
