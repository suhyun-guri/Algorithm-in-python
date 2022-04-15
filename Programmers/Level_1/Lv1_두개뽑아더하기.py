def solution(numbers):
    a = []
    for i in range(0,len(numbers)-1):
        for j in range(i+1,len(numbers)):
            a.append(numbers[i]+numbers[j])
        answer = sorted(list(set(a)))
    return answer

print(solution([2,1,3,4,1]))
print(solution([5,0,2,7]))