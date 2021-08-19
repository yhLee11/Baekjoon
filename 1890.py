n=int(input())
li=[]
ch=[]

for i in range(n):
    li.append(list(map(int,input().split())))
    ch.append([0 for _ in range(n)])

cnt=0
i=0
j=0
all=0
res=[]
one=[]
while all!=(n*n*2):

    num=li[i][j]
    ch[i][j]=1

    if i==n-1 and j==n-1:
        res.append(one)
        print(res)
        if one in res:
            one=[]
            i=0
            j=0
            for i in range(n):
                ch.append([0 for _ in range(n)])
            break

        one=[]
        cnt+=1
        i=0
        j=0
        num=li[i][j]
        ch=[]
        for i in range(n):
            ch.append([0 for _ in range(n)])

    if j+num<n and i<n:
        j+=num
        ch[i][j]=1
        num = li[i][j]
        one.append((i,j))
        #print(i,j,num)
    else:
        if i+num<n and j<n:
            i+=num
            ch[i][j]=1
            num=li[i][j]
            one.append((i,j))
        else:
            #print('out of range')
            break
    print(ch)
    print(res)
    print(cnt)
    all+=1
