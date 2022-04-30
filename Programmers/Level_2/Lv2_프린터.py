def solution(priorities, location):
    loc = [i for i in range(len(priorities))]
    answer = []
    
    while priorities:
        #맨 앞이 max값이면 answer에 append
        if priorities[0] == max(priorities):
            answer.append(loc.pop(0))
            priorities.pop(0)
        else:
            #아니라면, priorities, loc 맨 앞을 맨 뒤로 보내기
            priorities.append(priorities.pop(0))
            loc.append(loc.pop(0))
            
    return answer.index(location)+1
    


print(solution([2,1,3,2],2))
print(solution([1, 1, 9, 1, 1, 1],0))