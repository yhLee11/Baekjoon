import sys
input=sys.stdin.readline
s1=input().strip()
s2=input().strip()
LCS=[[0 for _ in range(len(s2)+1)] for _ in range(len(s1)+1)]

for i in range(1,len(s1)+1):
    for j in range(1,len(s2)+1):
        if s1[i-1]==s2[j-1]:
            LCS[i][j]=LCS[i-1][j-1]+1
        else:
            LCS[i][j]=max(LCS[i-1][j],LCS[i][j-1])
print(LCS[-1][-1])
# cnt=0
# i,j=6,6
# while LCS[i][j]:
#     num=LCS[i][j]
#     if LCS[i-1][j]==num:
#         i-=1
#     elif LCS[i][j-1]==num:
#         j-=1
#     else:
#         cnt+=1
#         i-=1
#         j-=1
# print(cnt)

    