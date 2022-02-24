import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=list(reversed([int(input()) for _ in range(n)]))
cnt=0

for c in coin:
    if k==0:
        print(cnt)
        exit(0)
    a,b=divmod(k,c)
    if a!=0:#몫이 있는 경우
        cnt+=a
        k=b
print(cnt)