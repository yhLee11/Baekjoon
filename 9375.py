import sys
from collections import defaultdict
input=sys.stdin.readline
tc=int(input())

for _ in range(tc):
    n=int(input())
    dic=defaultdict(list)
    for _ in range(n):
        item,type=map(str,input().split())
        dic[type].append(item)

    ans=1
    for k in dic.keys():
        ans*=(len(dic[k])+1)

    print(ans-1)