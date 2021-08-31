import sys
input=sys.stdin.readline
tc=int(input())
def num(m,n,x,y):
    while x<=m*n:
        if (x-y)%n==0:
            print(x,y,n)
            return x
        x+=m
    return -1
for _ in range(tc):
    m,n,x,y=map(int,input().split())
    print(num(m,n,x,y))
"""
https://pacific-ocean.tistory.com/126
정답:k
(k-x)%m = 0
(k-y)%n = 0
k == x 또는 y에 m과 n을 계속 더한 값 중 하나이다
x에 m을 계속 더해주고 y를 뺀 값에 n이 나누어 떨어진다면 그 값이 정답
"""
