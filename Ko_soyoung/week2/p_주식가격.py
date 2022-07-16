from collections import deque


def solution(prices):
    q = deque(prices)
    answer = []

    while q:
        price = q.popleft()
        second = 0
        for i in q:
            second += 1
            if price > i:
                break
        answer.append(second)
    return answer