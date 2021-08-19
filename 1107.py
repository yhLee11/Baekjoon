import sys
input=sys.stdin.readline
channel=int(input())
broken=int(input())
lst=list(input().strip())

def check(num):
    num=list(str(num))
    for i in num:
        if i in lst:
            return False
    return True

res=abs(channel-100)#+-버튼만으로 이동시
for i in range(10000001):
    if check(i): res=min(res,len(str(i))+abs(i-channel))
print(res)
