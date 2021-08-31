from collections import defaultdict
import sys
input=sys.stdin.readline
n=int(input())
x=list(map(int,input().split()))
s=list(set(x))
s.sort()
dic=defaultdict(int)
for i,v in enumerate(s):
    dic[v]=i
for i,v in enumerate(x):
    x[i]=dic[v]
print(*x)
