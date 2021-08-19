import sys
input=sys.stdin.readline
N,M=map(int,input().split())
dic={}

for i in range(N):
    address, password=input().split()
    dic[address]=password

for i in range(M):
    search=input().strip()
    print(dic[search])
