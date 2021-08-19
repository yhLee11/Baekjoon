# from itertools import permutations
from collections import Counter
import sys
input=sys.stdin.readline
tc=int(input())

for i in range(tc):
    n=int(input())
    clothes=[]
    for j in range(n):
        line=list(input().split())
        clothes.append(line[0])
    cnt=1
    res=Counter(clothes)
    # print(res)

    for k in res:
        cnt*=res[k]+1
    print(cnt-1)
