import sys
t=int(sys.stdin.readline())
sum=0
res=[]
for i in range(t):
    k=int(sys.stdin.readline())
    n=int(sys.stdin.readline())
    f0=[x for x in range(1, n+1)]

    for j in range(k):
        for p in range(1,n):
            f0[p]+=f0[p-1]
    print(f0[-1])
