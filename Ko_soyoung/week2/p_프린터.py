from collections import deque


def solution(priorities, location):
    answer = 0
    q = deque([(value, idx) for idx, value in enumerate(priorities)])
    
    while len(q):
        docs = q.popleft()
        if q and docs[0] < max(q)[0]:
            q.append(docs)
        else:
            answer += 1
            if docs[1] == location:
                break
    return answer