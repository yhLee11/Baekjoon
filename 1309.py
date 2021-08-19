n=int(input())
li=[[0]*n for _ in range(2)]
print(li)
cnt=1#한마리도 배치하지 않을때도 COUNT
chk1=[0]*n
chk2=[0]*n
chk2[0]=1
ptr=1
res=[1]*n

dp=[1 for _ in range(n+1)]

def fun(chk):
    y=1
    while True:
        #y=ptr #x=0,1 y=0,1,2...n
        if y==n:
            break
        if li[0][y-1]==False and li[1][y]==False and chk[y-1]==1:
            chk[y]=2
        else:#0만 넣을 수 있는 경우 chk[y-1]==2이면
            chk[y]=1
        y+=1
    print(chk)
print(fun(chk1),fun(chk2))

#start=[(0,0),(1,0),(0,1)]
# def rec(ptr,where,num):
#     if ptr==len(n):
#         return
#     if num==0:
#         li[0][ptr]=0
#     else:
#         li[0][ptr]=1
#         chk1[ptr]=True
#
#     if chk1[ptr-1]==False and chk2[ptr]==False:
#         res(ptr+1,0,0)
#         res(ptr+1,0,1)
#     elif chk1[ptr-1]==True and chk2[ptr]==False:
#         res(ptr)
#
#
# while True:
#     add=0
#     if one==len(n) and two==len(n):
#         cnt+=add
#         break
#     one,two=q.popleft()
#     if chk1[one-1]==False and chk2[one]==False:
#         li[one]=1
#         #0을 넣거나 1을 넣음
#         add=1
#     elif chk1[one-1]==True and chk2[one]==False: #1 0/0 0
#         li[two]=1
#         add=1
#         #0을 넣거나 1을 넣음 2가지 경우 존재
#     else:
