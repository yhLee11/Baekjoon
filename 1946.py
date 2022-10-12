import sys
input=sys.stdin.readline
T=int(input())
for _ in range(T):
    N=int(input())
    lst=[]
    cnt=1
    for _ in range(N):
        a,b=map(int,input().split())
        lst.append([a,b])
    lst.sort(key=lambda x:x[0])
    # print(lst)
    tmp=lst[0][1]
    for i in range(1,N):
        if tmp>lst[i][1]:#1등보다 높은 면접 점수
            tmp=lst[i][1]
            cnt+=1
    print(cnt)