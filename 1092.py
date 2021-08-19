import sys
N = int(input())
cranes = map(int, sys.stdin.readline().split()) #크레인 별 무게 제한
M = int(input())
boxes = map(int, sys.stdin.readline().split()) #화물 별 무게

# 무게 제한과 화물 무게 전부 내림차순으로 정렬
cranes = sorted(cranes, reverse=True)#986
boxes = sorted(boxes, reverse=True)#75422

#무게 제한이 제일 높은 크레인도 제일 무거운 화물을 들 수 없는 경우
if boxes[0] > cranes[0] :
    print(-1)
    exit()

answer = 0
# 화물이 전부 옮겨질 때까지
while len(boxes) > 0:
    answer += 1
    # 무게제한을 돌면서 옮길 수 있는 화물을 옮김
    for l in cranes:
        for j in range(len(boxes)):
            if l >= boxes[j]: # 화물을 옮길 수 있으면
                del boxes[j]
                break
print(answer)
