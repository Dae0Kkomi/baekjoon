def solution(n, w, num):
    
    answer = 0
    arr=[]
    if(n%w!=0):
        height=n//w+1
    else:
        height=n//w
    for a in range(height):
        if (a%2==0):
            arr.append(list(i for i in range(a*w+1, w*(a+1)+1)))
        else:
            arr.append(list(i for i in range(w*(a+1),a*w, -1)))
    for i in range(height):
        for j in range(w):
            if arr[i][j]==num:
                if(arr[height-1][j]>n):
                    return height-i-1
                else:
                    return height-i
            
