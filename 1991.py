import sys
def Btree(r):
    return [r,[],[]]
def insertLeft(root,newBranch):
    t=root.pop(1)
    if len(t)>0:
        root.insert(1,[newBranch,t,[]])
    else:
        root.insert(1,[newBranch,[],[]])
def insertRight(root,newBranch):
    t=root.pop(2)
    if len(t)>0:
        root.insert(2,[newBranch,t,[]])
    else:
        root.insert(2,[newBranch,[],[]])
def setRootVal(root,newVal):
    root[0]=newVal
def getLeftChild(root):
    return root[1]
def getRightChild(root):
    return root[2]
def getRootVal(root):
    return root[0]

n=int(sys.stdin.readline())
rTree=list(sys.stdin.readline().split())
r=Btree(rTree[0])
if rTree[1]!='.':
    insertLeft(r,rTree[1])
if rTree[2]!='.':
    insertRight(r,rTree[2])

for i in range(1,n):

    subTree=list(sys.stdin.readline().split())
    sub=Btree(subTree[0])
    if subTree[1]!='.':
        insertLeft(getLeftChild(r),subTree[1])
    if subTree[2]!='.':
        insertRight(getRightChild(r),subTree[2])

print(r)
aws=''
def preoder(root):#전위순회
    if not root:
        return
    else:
        print(getRootVal(root),end='')
        preoder(getLeftChild(root))
        preoder(getRightChild(root))

def inorder(root):#중위순회
    if not root:
        return
    else:
        inorder(getLeftChild(root))
        print(getRootVal(root),end='')
        inorder(getRightChild(root))
def postorder(root):#후위순회
    if not root:
        return
    else:
        postorder(getLeftChild(root))
        postorder(getRightChild(root))
        print(getRootVal(root),end='')


print('in',inorder(r))
print('post',postorder(r))
print('pre',preoder(r))
