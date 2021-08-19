import sys
n=int(sys.stdin.readline().strip())
people=[]
for i in range(n):
    x,y=map(int,sys.stdin.readline().split())
    people.append((x,y))

for i in range(n):
    cnt=0
    for j in range(n):
        if i==j:
            continue
        elif people[i][0]<people[j][0] and people[i][1]<people[j][1]:
            cnt+=1

    print(cnt+1,end=' ')
