import sys
# from itertools import permutations as pm
input=sys.stdin.readline
n=int(input())
A=sorted(list(map(int,input().split())),reverse=True)
B=sorted(list(map(int,input().split())))

ans=0
for i in range(len(A)):
    ans+=A[i]*B[i]
print(ans)


# plst=sorted(list(pm(A,len(A))))
# tmp=0
# for i in range(len(plst[0])):
#     tmp+=plst[0][i]*B[i]
# print(tmp)