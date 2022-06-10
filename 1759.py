import sys
input=sys.stdin.readline
L,C=map(int,input().split())
arr=sorted(list(map(str,input().split())))
vowel=['a','e','i','o','u']#모음
#최소 한개의 모음(vowel), 최소 두개의 자음(consonant)
s=[]
def dfs(depth,v_cnt,c_cnt):
    global s
    if depth==L:
        if v_cnt>=1 and c_cnt>=2:
            print(''.join(s))
        return
    for i in range(C):
        if depth==0 or s[depth-1]<arr[i]:
            s.append(arr[i])
            if  arr[i] in vowel:
                dfs(depth+1,v_cnt+1,c_cnt)
            else:
                dfs(depth+1,v_cnt,c_cnt+1)
            s.pop()

dfs(0,0,0)