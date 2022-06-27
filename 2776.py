import sys
input=sys.stdin.readline

T=int(input())
for _ in range(T):
    n=int(input())
    note1=sorted(list(map(int,input().split())))
    m=int(input())
    note2=list(map(int,input().split()))

    for num in note2:#찾는 숫자 num
        left=0
        right=n-1
        numExist=True
        while left<=right:
            mid=(left+right)//2
            if num==note1[mid]:
                print(1)
                numExist=False
                break
            
            if num>note1[mid]:
                left=mid+1
            else:
                right=mid-1

        if numExist:
            print(0)
            
