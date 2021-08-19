N=int(input())
li=[int(input()) for _ in range(N)]
sum=0
for i in li:
    sum+=i
sum=sum/N
print(round(sum))

li=sorted(li)
mid=len(li)//2
print(li[mid])

from collections import Counter

if N==1:
    print(li[0])
else:
    c=Counter(li).most_common()
    if c[0][1]==c[1][1]:
        print(c[1][0])
    else:
        print(c[0][0])


print(li[-1]-li[0])
