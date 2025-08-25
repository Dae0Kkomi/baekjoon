n,m,b=map(int,input().split())
arr=[]
for i in range(n):
    arr.append(list(map(int, input().split())))
block=[]# 숫자가 저장되어있는 곳
num=[] # 숫자의 종류
for i in range(n):
    for j in range(m):
        block.append(arr[i][j])
        if arr[i][j] not in num:
            num.append(arr[i][j])
count=[]  # 현재좌표보다 낮은 거의 개수

def inven(num):
    temp=-1
    time=[]
    for target in num:
        if (temp==target):
            pass
        min=[a - target for a in block if a - target<0] #if a - target<0 추가필요 뒤에
        if len(min)<=b: #인벤 개수 충분할 경우
            time.append([target-a for a in block if a - target<0])
        else: #부족할경우
            pass
        temp=target
        

        

inven(num)
