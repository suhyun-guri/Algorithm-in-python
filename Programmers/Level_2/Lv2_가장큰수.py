#정렬문제
'''
x*3 - 문자열에 3을 곱하면 333, 303030, 343434, 555, 999
여기서 정렬을 하면, 999 > 555 > 343434 > 333 > 303030
마지막에 str(int(''.join(list)))를 하는 이유는 0이 존재하므로 -> 문자열 0들을 join 하면 000 이렇게 나오기 때문에 이를 방지하기 위해
## x*2는 안되는 이유 : 각 num의 자릿수가 1,000이하기 때문에 -> [9,991]이라면, [99, 991991]로 여전히 991이 더 크다. [999, 991991991] 하면 999가 더 크다. (str 사전식으로 정렬)
'''
def solution(numbers):
    answer = []
    li = sorted(list(map(str, numbers)), reverse=True, key=lambda x:x*3)
    return str(int(''.join(li)))

print(solution([6,10,2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([0,0,0]))