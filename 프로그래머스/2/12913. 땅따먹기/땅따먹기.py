def solution(land):
    answer = 0
    temp_list=[5,6,7,8]
    for i in range(1, len(land)):
        for j in range(4):
            land[i][j]+=max(land[i-1][0:j]+land[i-1][j+1:])
    return (max(land[len(land)-1]))
            
            