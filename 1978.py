def isPrime(num):
    if num==1:
        return False
    else:
        for i in range(2,int(num**0.5)+1):
            if num%i==0:
                return False
        return True

n=int(input())
li=list(map(int,input().split()))
cnt=0
for val in li:
    if isPrime(val):
        cnt+=1
print(cnt)
