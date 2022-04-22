'''
처음에 단순 재귀함수로 풀었었는데, 재귀 호출 깊이를 초과하여 런타임에러 발생
'''
def solution(n):
    answer = [0] * (n+1)
    answer[1] = 1
    for i in range(2,n+1):
        answer[i] = answer[i-1] + answer[i-2]
    return answer[n] % 1234567

print(solution(3))
print(solution(5))