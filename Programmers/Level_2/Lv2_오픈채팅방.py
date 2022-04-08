'''
들어왔다가 나갔다가 다시 들어올 때 이름 바뀌면 그 전 것도 바꾼다..
'''
def solution(record):
    answer = []
    id_nickname = {}
    order_id = []
    for i in record:
        order, id = i.split()[0], i.split()[1]
        order_id.append((order, id))
        if order == 'Enter':
            name = i.split()[-1]
            id_nickname[id] = name
        elif order == 'Change':
            name = i.split()[-1]
            id_nickname[id] = name
            
    for order1, id1 in order_id:
        if order1 == 'Enter':
            answer.append(f'{id_nickname[id1]}님이 들어왔습니다.') 
        elif order1 == 'Leave':
            answer.append(f'{id_nickname[id1]}님이 나갔습니다.') 
    
    return answer
                       
            
            
    # return order_id, id_nickname
            
        
        
        
    return answer

print(solution(["Enter uid1234 Muzi", "Enter uid4567 Prodo","Leave uid1234","Enter uid1234 Prodo","Change uid4567 Ryan"]))