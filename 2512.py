def b(l,h):
    while l<=h:
        mid=(h+l)//2
        res=0
        for i in li:
            if i>=mid:
                res+=mid
            else:
                res+=i
        if res>m:
            h=mid-1
        else:
            l=mid+1

    print(h)

n=int(input())
li=input().split()
sum=0
for i in range(n):
    li[i]=int(li[i])
    sum+=li[i]
m=int(input())
if sum<=m:
    print(max(li))
else:
    low,high=0,max(li)
    b(low,high)
