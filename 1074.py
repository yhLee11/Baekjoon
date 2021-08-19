N,r,c = map(int,input().split())
cnt=0
while N>0:
    mat=(2**N)//2
    if N>1:
        if mat>r and mat<=c:
            cnt+=mat**2
            c-=mat
        elif mat<=r and mat>c:
            cnt+=(mat**2)*2
            r-=mat
        elif mat<=r and mat<=c:
            cnt+=(mat**2)*3
            r-=mat
            c-=mat
    elif N==1:
        if r==0 and c==1:
            cnt+=1
        elif r==1 and c==0:
            cnt+=2
        elif r==1 and c==1:
            cnt+=3
    N-=1
print(cnt)
