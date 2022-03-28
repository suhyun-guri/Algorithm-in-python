def solution(s):
    answer = []
    for word in s.split(' '):
        answer.append(''.join([i.upper() if idx % 2 == 0 else i.lower() for idx, i in enumerate(word)]))
    return ' '.join(answer)

print(solution('Try hello world'))
print(solution('aaa aaAAAAaaa aaaaaaaaaa'))