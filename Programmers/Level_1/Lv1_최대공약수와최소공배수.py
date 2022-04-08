def solution(n, m):
    n, m = min(n, m), max(n, m)
    i = n
    while i > 0:
        if m%i == 0 and n%i == 0:
            return [i, (n*m)/i]
        i -= 1
        
print(solution(3, 12))
print(solution(2, 5))