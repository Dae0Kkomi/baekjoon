def solution(schedules, timelogs, startday):
    result=0
    for b in range(len(schedules)):
        temptime=schedules[b]
        schedules[b]=temptime%100 + ((temptime - temptime%100)//100)*60

        
    for i in range(len(timelogs)):
        isTrue = True
        timelogs[i].pop(7-startday)
        timelogs[i].pop(6-startday)
        
        for a in range(5):
            temptime=timelogs[i][a]
            timelogs[i][a]=temptime%100 + ((temptime - temptime%100)//100)*60

        
        for time in timelogs[i]:
            if time - schedules[i] > 10:
                isTrue = False
                break
        if isTrue == True:
            result+=1
            continue
          
        
    return (result)
    