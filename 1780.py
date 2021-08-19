#종이의개수
n=int(input())
arr=[]
for _ in range(n):
    line=list(map(int,(input().split())))
    arr.append(line)
res={-1:0,0:0,1:0}

def cut(x,y,n):
    chk=arr[x][y]
    for i in range(x,x+n):
        for j in range(y,y+n):
            if chk!=arr[i][j]:
                for k in range(3):
                    for p in range(3):
                        print(x+n//3*k,y+n//3*p,n//3)
                        cut(x+n//3*k,y+n//3*p,n//3)
                return
    if chk==-1:
        res[-1]+=1
    elif chk==0:
        res[0]+=1
    else:
        res[1]+=1

cut(0,0,n)
print(res)
