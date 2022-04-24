def solution(n):
    answer = 0
    temp = []
    while n > 0:
        temp.append(n%3)
        n //= 3
    temp.reverse()
    for idx, i in enumerate(temp):
        answer += (i*(3**idx))
    return answer

print(solution(45))
print(solution(125))