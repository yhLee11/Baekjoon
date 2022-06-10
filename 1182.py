import sys
input=sys.stdin.readline
n,s=map(int,input().split())
lst=list(map(int,input().split()))
cnt=0
def dfs(idx,hap):
    # print(idx,hap)
    global cnt
    if idx>=n:
        return
    hap+=lst[idx]
    if hap==s:
        cnt+=1
    #현재 lst[idx]를 선택하지 않은 경우의 가지
    dfs(idx+1,hap-lst[idx])
    #현재 lst[idx]를 선택한 경우의 가지
    dfs(idx+1,hap)
dfs(0,0)
print(cnt)