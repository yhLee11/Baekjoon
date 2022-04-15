import sys
from collections import defaultdict
input=sys.stdin.readline
n,d,k,c=map(int,input().split())
max_eat=-sys.maxsize
sushi=[]
for _ in range(n):
    sushi.append(int(input()))
sushi*=2
cnt=0
dic=defaultdict(int)
dic[c]+=1
left,right=0,0
while right<k:
    dic[sushi[right]]+=1
    right+=1
# print(dic)
#2 7 9 25 7 9 7 30
while right<len(sushi):
    max_eat=max(max_eat,len(dic))
    dic[sushi[left]]-=1
    if dic[sushi[left]]==0:
        del(dic[sushi[left]])
    dic[sushi[right]]+=1
    left+=1
    right+=1
    # print(dic)
print(max_eat)