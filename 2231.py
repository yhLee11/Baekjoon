import sys
n=int(sys.stdin.readline())
cons=0
for i in range(1,n+1):
    num=list(map(int,str(i)))
    res=i+sum(num)
    if(res==n):
        cons=i
        break
print(cons)
