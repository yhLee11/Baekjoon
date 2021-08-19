n,m=map(int,input().split())
a=max(n,m)
b=min(n,m)
gcd=[a,b]
lcm=0
while gcd[1]!=0:
    mod=a%b
    gcd=[b,mod]
    a=b
    b=mod
lcm=m*n//gcd[0]
print(gcd[0])
print(lcm)
