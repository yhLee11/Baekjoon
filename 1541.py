import sys
input=sys.stdin.readline
lst=input().split('-')
num=[]
for i in lst:
    lst2=i.split('+')
    add=0
    for j in lst2:
        add+=int(j)
    num.append(add)
res=num[0]
for i in range(1,len(num)):
    res-=num[i]
print(res)
