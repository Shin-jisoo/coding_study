from itertools import combinations

def is_prime_number(x):
    for i in range(2,x):
        if x%i == 0:
            return False
    return True

def solution(nums):
    answer = 0
    tmp = []
    per_list = list(combinations(nums,3))
    for i in range(0,len(per_list)):
        sum_num = sum(per_list[i])
        flag = is_prime_number(sum_num)
        if flag == True:
            answer+=1
    
    return answer