import sys
input=sys.stdin.readline
n=int(input())
s='moo'
def rec(moo,cnt):
    if len(moo)>=n:
        print(moo[n-1])
        return
    mid='m'+'o'*(cnt+2)
    moo=moo+mid+moo
    rec(moo,cnt+1)
rec(s,1)