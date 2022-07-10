from collections import deque


def solution(progresses, speeds):
    answer = []
    days = deque()
    for i in range(len(progresses)):
        job = (100 - progresses[i]) / speeds[i]
        if job - int(job) == 0:
            days.append(int(job))
        else:
            days.append(int(job) + 1)

    cnt = 1
    distribute = days.popleft()
    while True:
        if len(days) == 0:
            answer.append(cnt)
            return answer
        if distribute >= days[0]:
            cnt += 1
            days.popleft()
        else:
            answer.append(cnt)
            cnt = 1
            distribute = days.popleft()