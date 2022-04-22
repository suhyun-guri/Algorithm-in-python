def solution(s):
    answer = list(map(int, s.split()))
    return f'{min(answer)} {max(answer)}'

print(solution("1 2 3 4"))
print(solution("-1 -2 -3 -4"))