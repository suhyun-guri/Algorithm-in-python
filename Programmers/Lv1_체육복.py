'''
[중요 포인트]
여벌 체육복을 가져온 학생이 체육복을 도난당했을 수 있습니다. 이때 이 학생은 체육복을 하나만 도난당했다고 가정하며, 남은 체육복이 하나이기에 다른 학생에게는 체육복을 빌려줄 수 없습니다.
'''
def solution(n, lost, reserve):
    #먼저 여벌이 있지만 도난당한 학생 제거
    reserve1 = set(reserve) - set(lost)
    lost1 = set(lost) - set(reserve)
    #전체 학생 수 - 진짜 없는 학생 수
    answer = n - len(lost1)
    #빌리기 시작
    for i in lost1:
        if i-1 in reserve1:
            reserve1.remove(i-1)
            answer += 1
        elif i+1 in reserve1:
            reserve1.remove(i+1)
            answer += 1
    return answer

print(solution(5, [2,4], [1,3,5]))
print(solution(5, [2,4], [3]))
print(solution(3, [3], [1]))
print(solution(6, [2,5,6], [2,4,6]))
print(solution(5, [2, 3, 4], [1, 2, 3]))
print(solution(5, [2,3], [3,4]))