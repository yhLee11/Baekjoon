n = int(input())
stack=[]
res=[]
cnt=0
flg=True
for i in range(0,n):
    num=int(input())
    while cnt<num:
        cnt+=1
        stack.append(cnt)
        res.append("+")
    if stack[-1]==num:
        stack.pop()
        res.append("-")
    else:
        flg=False
        break

if flg==False:
    print("NO")
else:
    print("\n".join(res))
