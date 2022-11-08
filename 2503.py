import sys
from itertools import permutations as pm
input=sys.stdin.readline          
N=int(input())
lst=list(pm([i for i in range(1,10)],3))
# print(lst)
for _ in range(N):
    num,st,b=map(int,input().split())
    num=list(str(num))
    remove=0
    for i in range(len(lst)):
        st_cnt,b_cnt=0,0
        i-=remove
        for j in range(3):
            num[j]=int(num[j])
            if num[j] in lst[i]:
                if j==lst[i].index(num[j]):
                    st_cnt+=1
                else:
                    b_cnt+=1
        if st_cnt!=st or b_cnt!=b:
            lst.remove(lst[i])
            remove+=1
print(len(lst))