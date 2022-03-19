def solution(new_id):
    #-----1단계-----
    new_id = new_id.lower()
    #-----2단계-----
    remove_str = '~!@#$%^&*()=+[{]}:?,<>/'
    new_id = ''.join([i for i in str(new_id) if i not in remove_str])
    #-----3단계-----
    while '..' in new_id:
        new_id = new_id.replace('..', '.')
    #-----4단계-----
    new_id = new_id[1:] if new_id.startswith('.') else new_id
    new_id = new_id[:-1] if new_id.endswith('.') else new_id
    #-----5단계-----
    if len(new_id) == 0:
        new_id = 'a'
    #-----6단계-----
    if len(new_id) >= 16:
        new_id = new_id[:15]
        if new_id.endswith('.'):
            new_id = new_id[:-1]
    #-----7단계-----
    while len(new_id) <= 2:
        new_id += new_id[-1]
    return new_id

print(solution("...!@BaT#*..y.abcdefghijklm"))
print(solution("z-+.^."))
print(solution("=.="))
print(solution("123_.def"))
print(solution("abcdefghijklmn...p"))
print(solution("././...dadasdfaf._Asdfa.p"))