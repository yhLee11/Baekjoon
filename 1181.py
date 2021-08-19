n = int(input())
li = [input() for _ in range(n)]
li = list(set(li))

li_len=[len(i) for i in li]
tu_li = []
for i in range(len(li)):
    tu_li.append((li[i],li_len[i]))

tu_li.sort(key=lambda x: (x[1],x[0]))
for i in tu_li:
    print(i[0])
#
# for i in range(len(tu_li)-1):
#     if tu_li[i][0]>tu_li[i+1][0]:
#         if tu_li[i][1]==tu_li[i+1][1]:
#             tmp = so_li.pop(i+1)
#             so_li.insert(i,tmp)
#
#
# for i in so_li:
#     print(i[0])
