import sys
input=lambda:sys.stdin.readline().strip()

t=int(sys.stdin.readline())

for i in range(t):
    p=input()
    n=int(input())
    de=input()[1:-1].split(',')
    p=p.replace('RR','')
    r=0#R의 개수
    f,b=0,0#f: 앞에서부터 버려야하는요소개수, b:뒤에서부터 버려야하는요소개수

    for ac in p:
        if ac=='R':
            r+=1
        elif ac=='D':
            if r%2==0:#R의 개수가 짝수이면 앞에서부터 빼야됨
                f+=1
            else:#R의 개수가 홀수이면 뒤에서부터 빼야됨
                b+=1

    if f+b<=n:
        de=de[f:n-b]
        if r%2==1:
            print('['+','.join(de[::-1])+']')
        else:
            print('['+','.join(de)+']')

    else:
        print('error')
