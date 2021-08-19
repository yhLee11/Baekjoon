from collections import deque
n,k=map(int,input().split())

q=deque()
q.append([n,0])
v=[0 for _ in range(100001)]
while q:
    p,d=q[0][0],q[0][1]
    if p==k:
        break
    q.popleft()
    v[p]=1
    if p-1>=0 and v[p-1]==0:
        q.append([p-1,d+1])
    if p+1<100000 and v[p+1]==0:
        q.append([p+1,d+1])
    if p*2<=100000 and v[p*2]==0:
        q.append([p*2,d+1])
print(q[0][1])
