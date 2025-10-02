from collections import Counter

n,m=map(int,input().split())
arr=[]
for _ in range(n):
    arr.append(list(input()))
W_arr=[]
for r in range(8):
    for c in range(8):
        # (r + c)의 합이 짝수이면 'W', 홀수이면 'B'
        if (r + c) % 2 == 0:
            W_arr.append('W')
        else:
            W_arr.append('B')

B_arr=[]
for r in range(8):
    for c in range(8):
        # (r + c)의 합이 짝수이면 'B', 홀수이면 'W'
        if (r + c) % 2 == 0:
            B_arr.append('B')
        else:
            B_arr.append('W')


resultarr=[]
for i in range((n-7)):  
    for j in range(m-7):
        temp=[]
        arrrr=[]
        result=0
        for k in range(i,i+8):
            temp.append(arr[k][j:j+8])
        for a in temp:
            arrrr+=a
            
        for aa,bb in zip(arrrr, B_arr):
            if (aa!=bb):
                result+=1
            else:
                pass
        resultarr.append(result)
        result=0
        for aa,bb in zip(arrrr, W_arr):
            if (aa!=bb):
                result+=1        
        resultarr.append(result)
print(min(resultarr))