def solution(priorities, location):
    from collections import deque
    
    answer = 0
    
    d = deque([(v,i) for i,v in enumerate(priorities)])
    
    #d[0]:priorities value
    #d[1]:index
    
    while len(d):
        item = d.popleft()
        if d and max(d)[0] > item[0]:
            d.append(item)
        else:
            answer+=1
            if item[1] == location:
                break
    
    return answer