#[50, 30, 24, 5, 28, 45, 98, 52, 60] 9
import sys
sys.setrecursionlimit(10**6)
input=sys.stdin.readline
tree=[]
while True:
    try:
        tree.append(int(input()))
    except:
        break
#print(tree,len(tree))
#chk=[0 for _ in range(len(tree))]

def post_order(start,end):
    if start>end:
        return

    root=tree[start]
    ptr=start+1
    while ptr<=end:
        if tree[ptr]>root:
            break

        ptr+=1
    #print('left sub',start+1,ptr-1)
    post_order(start+1,ptr-1)
    #print('right sub',ptr,end)
    post_order(ptr,end)
    print(root)

post_order(0,len(tree)-1)
