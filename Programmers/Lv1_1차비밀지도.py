'''
지도는 n*n 정사각형 배열, 공백과 벽(#) 두 종류로 이루어짐.
전체 지도는 지도1, 지도2를 겹쳐서 볼 수 있다.
지도1 또는 지도2에서 하나라도 벽이라면 전체 지도에서 벽, 모두 공백인 부분은 전체 지도에서 공백
배열은 정수 배열로 암호화됨. 이를 이진수로 바꾼 수가 지도에 해당 (1은 벽, 0은 공백)
'''

def solution(n, arr1, arr2):
    def set_binary(arr):
        result = []
        for i in arr:
            temp = []
            while i > 0:
                temp.append(i%2)
                i //= 2
            result.append(temp)
        for i in result:
            for _ in range(n-len(i)):
                i.append(0)
        return list(map(lambda x:x[::-1], result))
    
    map1, map2 = set_binary(arr1), set_binary(arr2)
    allmap = []
    for i, j in zip(map1, map2):
        allmap.append([a+b for a,b in zip(i,j)])
    answer = []
    for i in allmap:
        answer.append(''.join(list(map(lambda x:'#' if x>0 else ' ', i))))
    return answer

#-----다른 사람 풀이 참고하여 다시-----
def solution(n, arr1, arr2):
    answer = []
    for i,j in zip(arr1, arr2):
        #비트 연산자 or(|) 사용, [2:]로 0b를 제거
        a = str(bin(i|j)[2:])
        #rjust(width, [fillchar]) : 오른쪽으로 정렬, 너비, 공백을 메워줄 문자를 지정
        a = a.rjust(n,'0')
        a = a.replace('1','#').replace('0',' ')
        answer.append(a)
    return answer


print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))
print(solution(6, [46, 33, 33 ,22, 31, 50], [27 ,56, 19, 14, 14, 10]))