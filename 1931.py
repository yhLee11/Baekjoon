import sys
n=int(sys.stdin.readline())
lst=[]
cnt=0
start,end=map(int, sys.stdin.readline().split())
term=end-start
lst.append((term,start,end))

for i in range(0,n-1):#0,1,2,3...9 // n10전까지
    start,end=map(int, sys.stdin.readline().split())
    term=end-start

    if lst[cnt][2]<=start and lst[cnt][1]<=end:#새로 들어온게 안겹치면
        lst.append((term,start,end))
        cnt+=1
    else:#겹치면
        if lst[cnt][0]>term:
            lst.pop(cnt)
            lst.append((term,start,end))
print(lst)
print(cnt+1)
