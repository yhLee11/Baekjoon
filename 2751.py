import sys
n=int(sys.stdin.readline())
num=[int(sys.stdin.readline()) for _ in range(n)]
num=sorted(num)
for i in num:
    print(i)
