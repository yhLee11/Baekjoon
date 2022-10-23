from collections import defaultdict as dd
import sys
input=sys.stdin.readline
N=int(input())
ans=0
for _ in range(N):
    word=list(input().strip())
    idx=dd(list)
    for i in range(len(word)):
        # print(idx[word[i]])
        if idx[word[i]]!=-1 and idx[word[i]] and idx[word[i]][-1]!=i-1:
            idx[word[i]]=-1
            continue
        if idx[word[i]]==-1:continue
        idx[word[i]].append(i)
    if idx.values() and -1 not in idx.values():
        ans+=1
print(ans)