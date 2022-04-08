def solution(arr):
    answer = []
    answer.append(arr[0])
    for i in range(1, len(arr)):
        if arr[i-1] != arr[i]:
            answer.append(arr[i])
    return answer

#-----다른 사람 풀이 참고하여 다시-----
'''
빈 리스트일 때 list[-1] 하면 에러발생 but list[-1:] 하면 [] 출력
a = [1,2,3,4] 있다고 할 때, a[-1] == 4, a[-1:] == [4]
'''
def solution(arr):
    answer = []
    for i in arr:
        print(i, answer)
        if answer[-1:] == [i]: continue
        answer.append(i)
    return answer

print(solution([1,1,3,3,0,1,1]))
print(solution([1,0,0,0]))
print(solution([4,4,4,3,3]))