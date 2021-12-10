import sys
input=sys.stdin.readline
n,m=map(int,input().split())
#nCm = n!/(n-m)!m!, 2와 5의 쌍을 구하면 0의 갯수를 구할 수 있음
#25C12 = 25!/13!12!
#2의 갯수를 구함
def two_cnt(n):
    two=0
    while n!=0:
        n=n//2
        two+=n
    return two
#5의 갯수를 구함
def five_cnt(n):
    five=0
    while n!=0:
        n=n//5
        five+=n
    return five
# print(two_cnt(n),two_cnt(n-m),two_cnt(m))
print(min(two_cnt(n)-two_cnt(n-m)-two_cnt(m),five_cnt(n)-five_cnt(n-m),five_cnt(m)))
