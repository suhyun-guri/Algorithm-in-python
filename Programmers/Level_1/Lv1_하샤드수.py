def solution(x):
    return (int(x) % sum(map(int, list(str(x))))) == 0

print(solution(10))
print(solution(12))
print(solution(11))
print(solution(13))