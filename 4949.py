import sys
while True:
    str=sys.stdin.readline()
    stack=[]
    flg=1
    if str.rstrip()=='.':
        break

    for i in str:
        if i=='(' or i=='[':
            stack.append(i)
        if i==')':
            if stack and stack[-1]=='(':
                stack.pop()
            else:
                flg=0
                break
        if i==']':
            if stack and stack[-1]=='[':
                stack.pop()
            else:
                flg=0
                break

    print('yes' if flg and not(stack) else 'no') #not(stack):비어있는경우:not(0)=1 
