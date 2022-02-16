import sys
from collections import deque
input=sys.stdin.readline
a,b=map(int,input().split())
# *2, str+1 
q=deque()
q.append(b)
cnt=1
while q:
    num=q.popleft()
    if num==a:
        print(cnt)
        break
    elif num<a:
        print(-1)
        break

    if num%2==0:#짝수
        quo,rem=divmod(num,2)
        cnt+=1
        q.append(quo)
    else:#홀수
        str_n=str(num)
        if str_n[-1]=='1':
            str_n=str_n[:-1]
            q.append(int(str_n))
            cnt+=1
        else:
            print(-1)
            exit(0)