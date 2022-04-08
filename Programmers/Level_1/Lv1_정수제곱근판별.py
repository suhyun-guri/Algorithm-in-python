def solution(n):
    from math import sqrt
    if int(sqrt(n)) == sqrt(n):
        return (sqrt(n)+1)**2
    return -1

#-----다른 사람 풀이 참고하여 다시-----
def solution(n):
    sqrt = n**(1/2)
    if sqrt %  1 == 0:
        return (sqrt + 1)**2
    return -1

print(solution(121))
print(solution(25))
print(solution(50000000000000))