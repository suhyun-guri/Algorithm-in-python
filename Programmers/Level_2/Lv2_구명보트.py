'''
1. people을 sort하여 오름차순으로 정렬한다. 
2. 가장 가벼운 사람과 무거운 사람을 더해가며 limit보다 작거나 같으면 같이 보내고 무거우면 제일 무거운 사람부터 보낸다.

ex) [70, 50, 80, 50]
1. 정렬 : [50, 50, 70, 80], i = 0, j = 3
2. answer = 1 / 50 + 80 = 130 => limit보다 크다. i = 0, j = 2
3. answer = 2 / 50 + 70 = 120 => limit보다 크다. i = 0, j = 1
4. answer = 3 / 50 + 50 = 100 => limit보다 작거나 같다. i = 1, j = 0
5. return answer = 3
'''
def solution(people, limit):
    answer = 0
    people.sort()
    # print(people)
    i, j = 0, len(people)-1
    while i <= j:
        answer += 1
        if people[i] + people[j] <= limit:
            i += 1
        j -= 1
    return answer

print(solution([70, 50, 80, 50], 100))
print(solution([70, 80, 50], 100))