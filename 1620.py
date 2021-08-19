import sys
input=sys.stdin.readline
n,m=map(int,input().split())
name=[]
dic={}
for i in range(n):
    pk=input().strip()
    name.append(pk)
    dic[pk]=i+1
for i in range(m):
    qes=input().strip()
    if qes.isdigit():
        print(name[int(qes)-1])

    elif qes in name:
        print(dic[qes])
