h,w,n,m=map(int, input().split())


if w%(m+1)>0:
    temp1=w//(m+1)+1
else:
    temp1=w//(m+1)
if h%(n+1)>0:
    temp2=h//(n+1)+1
else:
    temp2=h//(n+1)

print(temp1*temp2)

