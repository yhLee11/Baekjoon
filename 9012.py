import sys
input=sys.stdin.readline
t=int(input())

for i in range(t):
    chk=True
    str=input()
    stack=[]
    for j in str:
        if j=='(':
            stack.append(j)
        elif j==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                chk=False
                break
    print('NO' if not chk or stack else 'YES')
