import math
def solution(progresses, speeds):
    temparr=[]
    result=[]
    for i in range(len(progresses)):
        temparr.append(math.ceil((100-progresses[i]) /speeds[i]))
    temp=temparr[0]
    count=1
    print(temparr)
    for number in temparr[1:]:
        if temp<number: # 
            result.append(count)
            temp=number
            count=1
        else:
            count+=1
    result.append(count)
    return (result)