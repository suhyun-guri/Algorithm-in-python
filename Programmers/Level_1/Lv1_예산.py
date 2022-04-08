def solution(d, budget):
    d = sorted(d)
    answer = 0
    for i in d:
        if budget - i >= 0:
            answer += 1
            budget -= i
    return answer

#-----다른 사람 풀이 참고하여 다시-----
def solution(d, budget):
    d.sort()
    while budget < sum(d):
        d.pop()
    return len(d)


print(solution([1,3,2,5,4],9))
print(solution([2,2,3,3],10))