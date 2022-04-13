import sys
from collections import deque
input=sys.stdin.readline

n,m = map(int,input().split())
ladder = [tuple(map(int,input().split())) for _ in range(n)]
snake = [tuple(map(int,input().split())) for _ in range(m)]
dice = [6,5,4,3,2,1]

def bfs(info):
    dq = deque()
    dq.append(info)
    visit=[False]*101
    while dq:
        start,end,depth=dq.popleft()
        visit[start]=True

        if end==100:
            print(depth)
            break

        for i in range(6):
            nstart = end
            nend = end + dice[i]

            if nend>100: continue
            # dq.append((nstart,nend,depth+1))
            if not visit[nstart]:
                
                flag=False
                for l,x in ladder:
                    if l==nend:
                        # print('l',l)
                        dq.append((nstart,x,depth+1))
                        flag=True
                for s,x in snake:
                    if s==nend:
                        # print('s',s)
                        dq.append((nstart,x,depth+1))
                        flag=True
                if not flag:
                    dq.append((nstart,nend,depth+1))
        
    
bfs((0,1,0))