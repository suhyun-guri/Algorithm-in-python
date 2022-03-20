def solution(board, moves):
    answer = []
    cnt = 0
    for i in moves:
        for n in board:
            if n[i-1] == 0:
                continue
            if len(answer) > 0 and answer[-1] == n[i-1]:
                n[i-1] = 0
                answer.pop()
                cnt += 2
                break
            answer.append(n[i-1])
            n[i-1] = 0
            break
    return cnt

print(solution(board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]],
               moves = [1,5,3,5,1,2,1,4]))
print(solution(board = [[0,0,0,0,0],[0,0,1,0,1],[0,2,5,0,1],[4,2,4,4,1],[3,5,1,3,1]],
               moves = [5,5,5,5]))