def solution(nums):
    def isPrime(number):
        for i in range(2, number):
            if number % i == 0:
                return False
        return True
    answer = []
    for i in range(len(nums)):
        for j in range(i+1, len(nums)):
            for k in range(j+1, len(nums)):
                number = nums[i]+nums[j]+nums[k]
                if isPrime(number):
                    answer.append(number)
    

    return len(answer)

print(solution([1,2,3,4]))
print(solution([1,2,7,6,4]))