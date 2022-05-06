'''
left부터 right까지의 모든 수 중에서
약수의 개수가 짝수인 수는 더하고
약수의 개수가 홀수인 수는 뺀 수를 return
'''
def solution(left, right):
    answer = 0
    dic = {}
    for i in range(left, right+1):
        cnt = 0
        for j in range(1, i+1):
            if i%j == 0:
                cnt+=1
        dic[i] = cnt
    for i,j in dic.items():
        if j%2 == 0:
            answer += i
        else:
            answer -= i
    return answer

#-----다른 사람 풀이 참고하여 다시-----
'''
Hint : 제곱수는 약수의 개수가 홀수!
'''
def solution(left, right):
    answer = 0
    for i in range(left, right+1):
        if int(i**0.5) == i**0.5:
            answer -= i
        else:
            answer += i
    return answer

print(solution(13,17))
print(solution(24,27))