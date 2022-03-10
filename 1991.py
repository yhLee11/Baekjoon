import sys
input=sys.stdin.readline
n=int(input())
tree={}
for _ in range(n):
    root,left,right=map(str,input().split())
    tree[root]=[left,right]

def preorder(root):
    if root=='.':
        return
    print(root,end='')
    lst=tree[root]
    preorder(lst[0])
    preorder(lst[1])

def inorder(root):
    if root=='.':
        return 
    lst=tree[root]
    inorder(lst[0])
    print(root,end='')
    inorder(lst[1])

def postorder(root):
    if root=='.':
        return
    lst=tree[root]
    postorder(lst[0])
    postorder(lst[1])
    print(root,end='')

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()