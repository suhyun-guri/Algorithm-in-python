'''
보너스 : S(현재 점수 1제곱), D(현재 점수 2제곱), T(현재 점수 3제곱)
옵션 : * (직전 최종 점수와 현재 점수 2배씩), # (점수 -1배)
"점수|보너스|[옵션]"으로 이루어진 문자열 3세트.
'''

def solution(dartResult):
    def addbonus(score, bonus):
        if bonus == 'S':
            return score
        elif bonus == 'D':
            return score ** 2
        elif bonus == 'T':
            return score ** 3
        return score
        
    answer = []        
    dartResult = dartResult.replace('10','a')
    for i in range(len(dartResult)):
        if dartResult[i].isdigit() or dartResult[i] == 'a':
            if dartResult[i] == 'a':
                score = addbonus(10, dartResult[i+1])
            else:
                score = addbonus(int(dartResult[i]), dartResult[i+1])
            try:
                if dartResult[i+2] in ['*', '#']:
                    if dartResult[i+2] == '*':
                        if len(answer) == 0:
                            score *= 2
                        answer[-1] *= 2
                        score *= 2
                    elif dartResult[i+2] == '#':
                        score *= (-1)
                answer.append(score)
            except:
                answer.append(score) 
    return sum(answer)          
            
print(solution('1D2D*3T')) #37
print(solution('1D2S#10S')) #9
print(solution('1S*2T*3S')) #23
print(solution('1D#2S*3S')) #5
print(solution('10D4S10D')) #204