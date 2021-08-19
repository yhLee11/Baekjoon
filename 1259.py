import sys
tc=[]
for line in sys.stdin:
    tc.extend(line.split())
    if tc[-1]=='0':
        break

for word in tc:
    if word=='0':
        break
    if word[::-1]==word:
        print('yes')
    else:
        print('no')
