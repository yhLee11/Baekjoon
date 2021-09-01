import sys
input=sys.stdin.readline
n,k=map(int,input().split())
coin=[int(input()) for _ in range(n)]
coin.reverse()
cnt=0

for i in range(n):
    if coin[i]==k:
        print(1)
        break
    elif coin[i]<k:

        m=-1
        n1=-1
        while i<=n:
            if n1==0:break
            if m==0 and n<0:
                k+=n1
                i+=1

            m=k//coin[i]#몫
            n1=k%coin[i]#나머지
            k=n1#현재금액

            cnt+=m
            m=n1
            i+=1
print(cnt)
