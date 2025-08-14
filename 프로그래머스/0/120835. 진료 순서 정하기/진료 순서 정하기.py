def solution(emergency):
    answer = []
    arr=[]
    for n in emergency:
        arr.append(n)
    arr.sort(reverse=True)
    for i in emergency:
        for a in range(len(emergency)):
            if(arr[a]==i):
                answer.append(a+1)
                print(a+1)
    return answer