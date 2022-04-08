def solution(n):
    answer = '수박'
    return answer*int(n/2) if n%2 == 0 else answer * int(n/2) + answer[0]

#-----다른 사람 풀이 참고하여 다시-----
def solution(n):
    answer = '수박' * n
    return answer[:n]
    
    
print(solution(3))
print(solution(6))
