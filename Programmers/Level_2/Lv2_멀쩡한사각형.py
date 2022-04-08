'''
최대공약수 사용
너비*높이 - (너비 + 높이 - 너비와 높이의 최대공약수)
최대공약수 함수 -> from math import gcd
'''

def solution(w,h):
    def gong(n, m):
        i = min(n, m)
        while i > 0:
            if m%i == 0 and n%i == 0:
                return i
            i -= 1
    if w == h:
        return w*h - w
    return w*h - (w+h-gong(w,h))

#-----다른 사람 풀이 참고하여 다시-----
def solution(w, h):
    from math import gcd
    return w*h - (w+h-gcd(w,h))


print(solution(8, 12)) #80
print(solution(3,3)) #6
print(solution(5,6)) #20
print(solution(4,5)) #12
