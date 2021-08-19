import sys

while True:
    num=list(map(int,sys.stdin.readline().split()))
    if num==[0,0,0]:
        break

    num.sort(reverse=True)

    if (num[0]**2)==(num[1]**2+num[2]**2):
        print('right')
    else:
        print('wrong')
