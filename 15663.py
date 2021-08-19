from itertools import permutations
import sys
input=sys.stdin.readline
n,m=map(int,input().split())
num=list(map(int,input().split()))
num=sorted(num)

res=list(set(permutations(num,m)))

res.sort(key=lambda x : (x[0]))
for i in res:
    i=list(i)
    for j in i:
        print(j,end=' ')
    print()
