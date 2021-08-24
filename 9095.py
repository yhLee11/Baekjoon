import sys
input=sys.stdin.readline
t=int(input())
num=[int(input()) for _ in range(t)]
# print(num)
def sol(n):
    if n==1:
        return 1
    elif n==2:
        return 2
    elif n==3:
        return 4
    else:
        return sol(n-1)+sol(n-2)+sol(n-3)
for i in num:
    print(sol(i))

"""
1: 1->1
2: 1+1,2->2
3: 3,1+1+1,1+2,2+1->4
4: 1+1+1+1,1+1+2,1+3,2+2...->7
5: 1+1+1+1+1,1+1+1+2,1+1+3,1+2+2,2+2+1,3+2....->13
점화식: n이 3보다 클 때, f(n)=f(n-1)+f(n-2)+f(n-3)
"""
