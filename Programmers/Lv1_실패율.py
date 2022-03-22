'''
실패율 = 스테이지에 도달했으나 아직 클리어하지 못한 플레이어의 수 / 스테이지에 도달한 플레이어 수

N = 전체 스테이지의 개수
stages = 게임을 이용하는 사용자가 현재 멈춰있는 스테이지의 번호가 담긴 배열 

return : 실패율이 높은 스테이지부터 내림차순
'''
# 첫 시도 - 시간초과
# def solution(N, stages):
#     failure = {}
#     for i in range(1, N+1):
#         notclear = sum(list(map(lambda x:x==i, stages)))
#         clear = sum(list(map(lambda x:x>=i, stages)))
#         if clear == 0 :
#             failure[i] = 0
#             continue
#         failure[i] = notclear / clear
#     answer = {k: v for k,v in sorted(failure.items(), key=lambda x:x[1], reverse=True)}
#     return list(answer.keys())

#최종 제출
def solution(N, stages):
    from collections import Counter
    count = Counter(stages)
    failure = {}
    n = len(stages)
    for i in range(1,N+1):
        if n == 0: #예외처리
            failure[i] = 0
            continue
        failure[i] = count[i] / n
        n -= count[i]
    answer = {k: v for k,v in sorted(failure.items(), key=lambda x:x[1], reverse=True)}
    return list(answer.keys())

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))
print(solution(4, [4,4,4,4,4]))