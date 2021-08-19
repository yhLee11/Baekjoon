import sys
input=sys.stdin.readline
N,M,B=map(int,input().split())
map=[list(map(int,input().split())) for _ in range(N)]
dic={}
t=9223372036854775807
time,max_h=0,0
res=[]
for h in range(257):
    bottom=0
    top=0
    for i in range(N):
        for j in range(M):
            if map[i][j]<h:
                bottom+=h-map[i][j]
            elif map[i][j]>h:
                top+=map[i][j]-h
    #print(bottom,top,B+top)
    if bottom>top+B:
        continue
    time=2*top+bottom
    if time<=t:
        t=time
        max_h=h
print(t,max_h)
#
# res.sort(key=lambda x:(x[0],x[1]))
# if res[0][0]==res[1][0]:
#     for idx in range(len(res)):
#         if res[0][0]==res[idx+1][0]:
#             max_h=max(res[idx][1],res[idx+1][1])
#         elif res[0][0]!=res[idx][0]:
#             break
#     print(res[0][0],max_h)
# else:
#     print(res[0][0],res[0][1])
