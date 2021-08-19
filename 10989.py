import sys
input=sys.stdin.readline
n=int(input())
lst=[0 for _ in range(10001)]
for i in range(n):
    num=int(input())
    lst[num]+=1

for i in range(len(lst)):
    for j in range(lst[i]):
        print('lsti',lst[i])
        print(i)
