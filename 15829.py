import sys
input=sys.stdin.readline
l=int(input())
str=input().strip()
dic={}
i=0
for c in range(ord('a'), ord('z')+1):
    i+=1
    dic[chr(c)]=i

r=31
m=1234567891
hash=0
for idx,val in enumerate(str):
    hash+=dic[val]*(r**idx)

print(hash%m)
