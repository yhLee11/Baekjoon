import sys
input=sys.stdin.readline
st=input().strip()
lst=['c=','c-','dz=','d-','lj','nj','s=','z=']
for i in lst:
    st=st.replace(i,'.')
print(len(st))