a=int(input())
arr=[]
codes=[]
for _ in range(a):
    codes.append(input().split())
for code in codes:
    if code[0]=='push':
        arr.append(int(code[1]))
    elif code[0]=='top':
        print(arr[-1]) if len(arr)!=0 else print(-1)
    elif code[0]=='size':
        print(len(arr))
    elif code[0]=='empty':
        print(1 if len(arr)==0 else 0)
    elif code[0] =='pop':
        if len(arr)==0:
            print(-1)
        else:
            print(arr[-1])
            arr.pop()
    
