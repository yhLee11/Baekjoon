n,m=map(int, input().split())
b=[]
b.extend([input() for _ in range(n)])
res=[]

for k in range(n-7):
    for p in range(m-7):
        cnt1=0
        cnt2=0
        for i in range(k,k+8):
            for j in range(p,p+8):
                if (i+j)%2==0:
                    if 'W'!=b[i][j]:
                        cnt1+=1
                    if 'B'!=b[i][j]:
                        cnt2+=1
                else:
                    if 'B'!=b[i][j]:
                        cnt1+=1
                    if 'W'!=b[i][j]:
                        cnt2+=1
        res.append(cnt1)
        res.append(cnt2)

print(min(res))
