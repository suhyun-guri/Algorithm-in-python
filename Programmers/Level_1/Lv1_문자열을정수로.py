def solution(s):
    # if s[0] == '-':
    #     return -int(s[1:])
    # elif s[0] == '+':
    #     return int(s[1:])
    return int(s)

print(solution('+123123'))
print(solution('-123123'))
print(solution('123123'))
