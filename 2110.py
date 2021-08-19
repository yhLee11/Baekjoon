n,c=map(int,input().split())
li=[int(input().strip()) for _ in range(n)]

def router(dist):
    cnt=1
    start=li[0]
    for i in range(1,n):
        if start+dist<=li[i]:
            cnt+=1
            start=li[i]#갱신
    return cnt
li=sorted(li)
start,end=1,li[-1]-li[0]
while start<=end:
    mid=(start+end)//2
    if router(mid)>=c:
        res=mid
        start=mid+1
    else:
        end=mid-1
print(res)
# while low<=high:
#     mid=(low+high)//2
#     sub1=0
#     sub2=0
#     for elem in li:
#         sub1=li[mid]-li[low]
#         sub2=li[high]-li[mid+1]
#         if sub1>=sub2:
#             if max_dist[0][-1]<sub1:
#                 max_dist.pop()
#                 max_dist.append((low,mid,sub1))
#             high=mid-1
#             print(low,mid,high)
#             print('sub1>=sub2',max_dist)
#         else:
#             if max_dist[0][-1]<sub2:
#                 max_dist.pop()
#                 max_dist.append((mid+1,high,sub2))
#             low=mid+1
#             print(low,mid,high)
#             print('sub1<sub2',max_dist)
