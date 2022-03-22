def solution(absolutes, signs):
    answer = [n if signs[i] else -n for i, n in enumerate(absolutes) ]
    return sum(answer)

#-----다른 사람 풀이 참고하여 다시 (zip 사용)-----
def solution(absolutes, signs):
    return sum([n if sign else -n for n, sign in zip(absolutes, signs)])

print(solution([4,7,12], [True,False,True]))
print(solution([1,2,3], [False,False,True]))