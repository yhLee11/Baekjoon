from collections import deque
import sys
input=sys.stdin.readline

prec=input().strip()
print(prec)
stk=[]
res=''
for x in prec:
    if x.isalpha():
        res+=x
    else:
        if x=='(':
            stk.append(x)
        elif x=='*' or x=='/':
            while stk and (stk[-1]=='*' or stk[-1]=='/'):
                res+=stk.pop()
            stk.append(x)
        elif x=='+' or x=='-':
            while stk and stk[-1]!='(':
                res+=stk.pop()
            stk.append(x)
        elif x==')':
            while stk and stk[-1]!='(':
                res+=stk.pop()
            stk.pop()

while stk:
    res+=stk.pop()
print(res)
