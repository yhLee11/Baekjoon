x,y,w,h=map(int,input().split())
xmin = w-x
ymin = h-y
print(min(xmin,ymin,x,y))
