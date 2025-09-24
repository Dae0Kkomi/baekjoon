import sys
input = sys.stdin.readline

n,m,b=map(int,input().split())

block = []
for _ in range(n):      # block들을 1차원 배열로 변경
    block.extend(map(int, input().split()))
    
block.sort(reverse=True)
smin = min(block)
smax = max(block)
times=[]
temps=[]
temptime=999999990
for target_block in range(smin,smax+1):
    temp=b
    time=0
    for current_block in block:
        block_cnt=current_block-target_block             #
        if block_cnt>0:
            time+=block_cnt*2
            temp+=block_cnt
            
        elif block_cnt<0:
            if(abs(block_cnt)<=temp):
                temp-=abs(block_cnt)
                time+=abs(block_cnt)
            else:
                time=-1       # time 을 -1로 설정 (이건 안되는 경우)
                pass
    if(temp>=0 and time!=-1): # 인벤토리가 부족하지않을때
        if (temptime>=time):
            temptime=time
            returns=target_block
    elif(time==-1):
        break
        
            
print(temptime, returns)
