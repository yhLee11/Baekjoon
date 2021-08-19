import sys
a,b,v=map(int,sys.stdin.readline().split())
days=0

if (v-a)%(a-b)==0: #ex 5 1 5 #나머지가 0
    print(int((v-a)/(a-b))+1)
else:#나머지가 0이 아닌경우
    print(int((v-a)/(a-b))+2)
