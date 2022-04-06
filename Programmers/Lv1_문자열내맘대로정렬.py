def solution(strings, n):
    # key = lambda x: (기준1, 기준2)
    return sorted(strings, key=lambda x:(x[n], x[:]))

print(solution(["sun", "bed", "car"], 1))
print(solution(["abce", "abcd", "cdx"], 2))