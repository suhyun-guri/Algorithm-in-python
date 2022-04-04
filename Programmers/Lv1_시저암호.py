# 처음에 내가 풀었던 코드
# def solution(s, n):
#     alphabet = 'abcdefghijklnmopqrstuvwxyz'*2
#     answer = list(s)
#     for i in range(len(s)):
#         if s[i] in alphabet:
#             answer[i] = alphabet[alphabet.index(s[i]) + n]
#         elif s[i] in alphabet.upper():
#             answer[i] = alphabet.upper()[alphabet.upper().index(s[i]) + n]
#         else:
#             continue
    
#     return ''.join(answer)

#-----다른 사람 풀이 참고하여 다시-----

def solution(s, n):
    answer = [ord(i) for i in s] #먼저 ASCII Code 리스트로 변경해주기
    for i in range(len(answer)):
        if answer[i] == ord(' '): #공백일 경우 그대로
            continue
        elif answer[i] <= 90 and answer[i] + n > ord('Z'): #대문자일 경우 (대문자 ASCII Code : 65~90)
            answer[i] = answer[i] + n -26
        elif answer[i] <= 122 and answer[i] + n > ord('z'): #소문자일 경우 (소문자 ASCII Code : 97~122)
            answer[i] = answer[i] + n -26
        else:
            answer[i] = answer[i] + n #Z에 걸리지 않으면 n 더하기
    return ''.join(map(chr, answer))


print(solution("AaZz", 1))
print(solution("z", 1))
print(solution("a B z", 1))
print(solution("bC", 25))

# 123 - 97
