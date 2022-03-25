def solution(n):
    return int(''.join(sorted(list(str(int(n))), reverse=True)))

print(solution(11830072))
print(solution(1234))