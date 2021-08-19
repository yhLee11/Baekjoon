def b(arr,val,l,h):
    if l>h:
        return 0
    m=l+h//2
    if arr[m]>val:
        return b(arr,val,l,m-1)
    elif arr[m]<val:
        return b(arr,val,m+1,h)
    else:
        return 1
N=int(input())
A=list(map(int,input().split()))
A=sorted(A)
M=int(input())
B=list(map(int,input().split()))
for m in M:
    if b(A, m, 0, N-1):
        print(1)
    else:
        print(0)
