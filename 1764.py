N, M=map(int,input().split())
l=set()
s=set()
for _ in range(N):
    l.add(input())
for _ in range(M):
    s.add(input())

res=[]
res=sorted(list(l&s))

print(len(res))
for p in res:
    print(p)
