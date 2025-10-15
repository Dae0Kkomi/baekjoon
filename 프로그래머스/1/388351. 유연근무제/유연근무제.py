def solution(schedules, timelogs, startday):
    result=0
    for i in range(len(timelogs)):
        isTrue = True
            
        timelogs[i].pop(7-startday)
        timelogs[i].pop(6-startday)
        print(timelogs)
        for time in timelogs[i]:            
            if time - schedules[i] > 10:
                isTrue = False
                break
        if isTrue == True:
            result+=1                    
    return (result)
    