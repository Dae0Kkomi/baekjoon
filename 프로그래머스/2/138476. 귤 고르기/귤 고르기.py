from collections import Counter
def solution(k, tangerine):
    result=0
    count=Counter(tangerine)
    counted=sorted(count.values(), reverse=True)
    
    if max(counted)>=k:
        return 1
    for i in range(len(counted)+1):        
        if (k<=0):
            return result
            break
        else:
            k-=counted[i]
            result+=1

        
    
    
    
    
            
            