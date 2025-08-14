def solution(t, p):
    count=0
    for a in range(len(t)-len(p)+1):
        if (int(t[a:a+len(p)])<=int(p)):
            count+=1
    return count