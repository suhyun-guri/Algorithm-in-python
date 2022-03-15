def solution(id_list, report, k):
    user_dict, reported_dict = {s:[] for s in id_list}, {s:0 for s in id_list}
    for i in report:
        user, reported = i.split(' ')
        if reported in user_dict[user]:
            continue
        user_dict[user].append(reported) 
        reported_dict[reported] += 1
    mail_user = {s:0 for s in id_list}
    for u, v in reported_dict.items(): 
        if v >= k:
            for id in id_list:
                if u in user_dict[id]:
                    mail_user[id] += 1
    return list(mail_user.values())

print(solution(["muzi", "frodo", "apeach", "neo"], ["muzi frodo","apeach frodo","frodo neo","muzi neo","apeach muzi"], 2))
print(solution(["con", "ryan"], ["ryan con", "ryan con", "ryan con", "ryan con"], 3))
