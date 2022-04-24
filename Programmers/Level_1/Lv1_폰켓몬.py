'''
set을 통해 unique한 폰켓몬의 종류 수를 구한다.
만약 골라야 하는 폰켓몬의 수가 unique한 폰켓몬의 수보다 많으면 unique한 폰켓몬의 수를 리턴
아니라면, 골라야 하는 폰켓몬 수를 반환하면 된다.
'''
def solution(nums):
    n = len(nums) // 2
    unique_num = list(set(nums))
    if n >= len(unique_num):
        return len(unique_num)
    else:
        return n
    
#-----다른 사람 풀이 참고하여 다시-----
def solution(nums):
    return min(len(nums)/2, len(set(nums)))

print(solution([3,1,2,3]))
print(solution([3,3,3,2,2,4]))