#처음 풀었던 코드 -> 시간초과, 효율성 0
def solution(n):
    answer = list(range(2,n+1))
    for i in range(2,n+1):
        for j in range(2, i):
            if i % j == 0:
                answer.remove(i)
                break
    return len(answer)

#-----다른 사람 풀이 참고하여 다시-----
'''
에라토스테네스의 체 알고리즘 사용
참고 : https://freedeveloper.tistory.com/392, https://ko.wikipedia.org/wiki/%EC%97%90%EB%9D%BC%ED%86%A0%EC%8A%A4%ED%85%8C%EB%84%A4%EC%8A%A4%EC%9D%98_%EC%B2%B4 
: 소수를 판별하는 알고리즘으로 소수들을 대량으로 빠르고 정확하게 구하는 방법
1. 자기 자신(2)를 제외한 2의 배수 제거
2. 자기 자신(3)을 제외한 3의 배수 제거 
...
반복
에라토스테네스의 체 알고리즘의 시간복잡도는 선형 시간에 가까울 정도로 매우 빠르다 -> O(NloglogN)
'''
def solution(n):
    answer = set(range(2,n+1))
    for i in range(2, n+1):
        if i in answer:
            answer -= set(range(2*i, n+1, i))
    return len(answer)


print(solution(100))
print(solution(5))