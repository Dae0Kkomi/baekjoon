def solution(e, starts):
    # 1. [핵심 병목] 모든 수의 약수 개수 계산 (O(e log e))
    # 이 부분이 연산량의 대부분을 차지합니다.
    divisors = [0] * (e + 1)
    for i in range(1, e + 1):
        for j in range(i, e + 1, i):
            divisors[j] += 1

    # 2. 각 시작점 s에 대해 [s, e] 범위의 정답을 미리 계산 (O(e))
    answer_sheet = [0] * (e + 1)
    
    # 마지막 값으로 초기화
    max_divisor_num = e
    answer_sheet[e] = e
    
    # e-1부터 1까지 역순으로 순회
    for i in range(e - 1, 0, -1):
        # 기존의 최댓값(i+1부터 e까지의 정답)과 현재 값(i)을 비교
        # 약수의 개수가 현재 값(i)이 더 크거나 같다면, 정답을 i로 갱신
        # (개수가 같을 경우 숫자가 더 작은 i가 정답이므로 >= 조건 사용)
        if divisors[i] >= divisors[max_divisor_num]:
            max_divisor_num = i
        
        answer_sheet[i] = max_divisor_num
            
    # 3. starts에 맞는 정답을 answer_sheet에서 찾아서 반환 (O(len(starts)))
    result = [answer_sheet[s] for s in starts]
        
    return result
     
