'''
progresses, speeds를 큐로 가정.
모든 기능이 배포될 때까지 (progresses가 빌 때까지) 반복
- progresses 길이만큼 순회하여 각 기능의 진행 상황을 더해준다.
- 완성된 기능들이 있으면 배포한다. (while문 사용, pop으로 제거, cnt에 1 더해줌)
- 배포된 개수가 0보다 크면 answer에 넣는다.
'''
def solution(progresses, speeds):
    answer = []
    while progresses:
        for i in range(len(progresses)):
            progresses[i] += speeds[i]
        cnt = 0
        while progresses and progresses[0] >= 100:
            progresses.pop(0)
            speeds.pop(0)
            cnt += 1
        if cnt > 0:
            answer.append(cnt)
    return answer        
    

print(solution([93, 30, 55], [1, 30, 5]))
print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))

