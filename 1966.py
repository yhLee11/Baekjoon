import sys
# from collections import deque
input=sys.stdin.readline

tc = int(input())
for i in range(tc):
    m,n=map(int,input().split())
    lst=list(map(int,input().split()))
    chk=[0 for _ in range(m)]
    chk[n]=1
    cnt=0

    while True:
        if lst[0]==max(lst):
            cnt+=1

            if chk[0]!=1:
                lst.pop(0)
                chk.pop(0)
                print(lst)
            else:
                print(cnt)
                break
        else:
            lst.append(lst.pop(0))
            chk.append(chk.pop(0))

#출력하고 재정렬해서 1234->4123 4출력후, 123->312 3출력 
