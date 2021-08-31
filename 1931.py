import sys
input=sys.stdin.readline
n=int(input())
lst=[]
for _ in range(n):
    time=list(map(int,input().split()))
    start,end=time[0],time[1]
    lst.append([start,end])
lst.sort(key=lambda x: [x[1],x[0]])

cnt=0
end=0
for i,v in enumerate(lst):
    if v[0]>=end:
        cnt+=1
        end=v[1]
print(cnt)
