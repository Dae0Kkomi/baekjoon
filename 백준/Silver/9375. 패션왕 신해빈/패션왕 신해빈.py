for a in range(int(input())):
    arr={}
    for b in range(int(input())):
        name,clothes=input().split()
        if (arr.get(clothes)==None):  #처음들어오는 녀석일때
            arr[clothes]=1
        else:
            arr[clothes]+=1
    brr=list(arr.values())
    temp=1
    for value in brr:
        temp*=(value+1)
    print(temp-1)