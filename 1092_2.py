import sys
N = int(input())
cranes = list(map(int, sys.stdin.readline().split()))
M = int(input())
boxes = list(map(int, sys.stdin.readline().split()))

cranes.sort(reverse=True)
boxes.sort(reverse=True)

if cranes[0]<boxes[0]:
    print(-1)
    exit()

res=0
while len(boxes)!=0:
    res+=1
    for c in cranes:
        for b in range(len(boxes)):
            if c>=boxes[b]:
                del boxes[b]
                break

print(res)
