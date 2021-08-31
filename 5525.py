import sys
input=sys.stdin.readline
n=int(input())
m=int(input())
s=input().strip()

cnt,res=0,0
i=1
while i<m-1:
    if s[i-1]=='I' and s[i]=='O' and s[i+1]=='I':
        cnt+=1
        if cnt==n:#cnt=1일때 IOI
            res+=1
            cnt-=1#다시다음패턴찾기
        i+=1
    else:
        cnt=0#초기화, 패턴이 중간에 끊긴 경우
    i+=1

print(res)
