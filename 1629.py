'''
a = 10 , b = 11 , c = 12
10^11 % 12
= ((10^5)%12 x (10^5)%12 x 10)% 12
= ((10^2)%12 x (10^2)%12 x 10) %12 x (10^2)%12 x (10^2)%12 x 10) %12 x 10) %12
'''
import sys
input=sys.stdin.readline
a,b,c=map(int,input().split())

def multi(a,n):
    if n==1:
        return a%c
    else:
        mod=multi(a,n//2)
        if n%2==0:
            return (mod*mod)%c
        else:
            return (mod*mod*a)%c
print(multi(a,b))