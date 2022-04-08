'''
원래 이용료는 price, N번째 이용 시 이용료의 N배 - count
부족한 금액을 return
'''
def solution(price, money, count):
    # answer = sum([price*i for i in range(1,count+1)]) - money
    # return answer if answer > 0 else 0
    return max(0, sum([price*i for i in range(1,count+1)]) - money)

print(solution(3, 20, 4))
print(solution(3, 30, 4))