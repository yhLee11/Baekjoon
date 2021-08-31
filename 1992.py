import sys
input=sys.stdin.readline
n=int(input())
lst=[list(input().strip()) for _ in range(n)]
# print(lst)
tree=''
def divide(x,y,n):
    global tree
    # print(x,y)
    bit=lst[x][y]

    for i in range(x,x+n):
        for j in range(y,y+n):
            if bit!=lst[i][j]:
                tree+='('
                divide(x,y,n//2)
                divide(x,y+n//2,n//2)
                divide(x+n//2,y,n//2)
                divide(x+n//2,y+n//2,n//2)
                tree+=')'
                return

    if bit=='0':
        tree+='0'
    else:
        tree+='1'
divide(0,0,n)
print(tree)
