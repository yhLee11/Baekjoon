import sys
t=int(sys.stdin.readline())

for i in range(t):
    n=int(sys.stdin.readline())
    lst=[]
    s,m=map(int,sys.stdin.readline().split())
    cnt=1
    lst.append((s,m))#처음들어온 사람이 1순위
    max=lst[0][1]
    lst.sort()
    for j in range(n):
        s,m=map(int,sys.stdin.readline().split())
        lst.append((s,m))
        if max>lst[j+1][1]:
            cnt+=1
            max=lst[j+1][1]
        print(cnt)
