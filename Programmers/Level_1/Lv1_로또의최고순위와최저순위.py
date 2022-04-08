#-----내가 푼 풀이-----

# def solution(lottos, win_nums):
#     rank = {correct:(i+1) for i, correct in enumerate(range(6,0,-1))}
#     rank[0] = 6
#     answer = []
#     correct_nums = []
#     for i in lottos:
#         if i in win_nums:
#             correct_nums.append(i)
#         elif i == 0:
#             correct_nums.append(i)
#     answer.append(rank[len(correct_nums)])
#     answer.append(rank[len([i for i in correct_nums if i != 0])])
#     return answer

#-----다른 사람 풀이 참고하여 다시-----

def solution(lottos, win_nums):
    rank = [6,6,5,4,3,2,1]
    zero_cnt = lottos.count(0)
    correct = [i for i in lottos if i in win_nums]
    return [rank[len(correct)+zero_cnt], rank[len(correct)]]


print(solution([44, 1, 0, 0, 31, 25], [31, 10, 45, 1, 6, 19]))
print(solution([0, 0, 0, 0, 0, 0], [38, 19, 20, 40, 15, 25]))
print(solution([45, 4, 35, 20, 3, 9], [20, 9, 3, 45, 4, 35]))