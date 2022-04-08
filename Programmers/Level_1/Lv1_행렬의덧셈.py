def solution(arr1, arr2):
    answer = []
    for i, j in zip(arr1, arr2):
        answer.append([ii+jj for ii, jj in zip(i,j)])
    return answer

print(solution([[1,2],[2,3]], [[3,4],[5,6]]))
print(solution([[1],[2]], [[3],[4]]))