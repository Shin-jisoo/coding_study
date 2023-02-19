from itertools import combinations


def solution(number):
    answer = 0
    nums = list(combinations(number, 3))
    for i in nums:
        if sum(i) == 0:
            answer += 1
    return answer