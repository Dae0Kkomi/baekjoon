arr=[]
for a in range(30000):
    arr.append(list(map(int, input().split())))
    if arr[a]==[0,0,0]:
        break
    a,b,c=map(int, arr[a])
    if a*a+b*b==c*c:
       print('right')
    else:
        print('wrong')