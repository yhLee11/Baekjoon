import sys
input=sys.stdin.readline
n,m=map(int,input().split())
square=[list(map(int,list(input().strip()))) for _ in range(n)]
# print(square)

res=[]
def search(i,j,term):
    global res
    if 0<=i+term<n and 0<=j-term<m:
        bottomleft=[i+term,j-term]
        bottomright=[i+term,j]
        # print(bottomleft,bottomright)
        if square[i][j]==square[i+term][j-term]==square[i+term][j]:
            res.append((term+1)*(term+1))

for idx,val in enumerate(square):
    # print('idx,val',idx,val)
    for subidx, oneval in enumerate(val):
        # print('sub,oneval',subidx,oneval)
        for i in range(subidx+1,m):
            # print('i',i)
            if oneval==square[idx][i]:
                search(idx,i,i-subidx)

if not res:
    print(1)
else:
    print(max(res))
