import sys
import heapq
input=sys.stdin.readline
t=int(input())
res=[]
for _ in range(t):
    tc=int(input())
    maxh,minh=[],[]
    visit=[False]*1000000
    for i in range(tc):
        op,num=input().split()
        num=int(num)

        if op=='I':
            heapq.heappush(minh,(num,i))#num,id
            heapq.heappush(maxh,(-num,i))
            visit[i]=True#힙에서 삭제되지 않은 상태

        elif op=='D':
            if num==-1:
                while minh and not visit[minh[0][1]]:#visit=False:삭제된 상태
                    # print('min',minh)
                    heapq.heappop(minh)
                if minh:#visit가 True였기때문에 False로 바꾸고 삭제함
                    visit[minh[0][1]]=False
                    heapq.heappop(minh)
            else:
                while maxh and not visit[maxh[0][1]]:
                    # print('max',maxh)
                    heapq.heappop(maxh)
                if maxh:
                    visit[maxh[0][1]]=False
                    heapq.heappop(maxh)
    #모든 연산이 끝나고 쓰레기 노드가 들어있을 수 있어서
    #모두 비우고 각 힙의 첫번째 원소를 출력
    while minh and not visit[minh[0][1]]:
        # print('minres',minh)
        heapq.heappop(minh)
    while maxh and not visit[maxh[0][1]]:
        # print('maxres',maxh);
        heapq.heappop(maxh)
    if minh and maxh:
        print(-maxh[0][0],minh[0][0])
    else:
        print("EMPTY")
