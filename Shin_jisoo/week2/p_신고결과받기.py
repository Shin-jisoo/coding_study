def solution(id_list, report, k):
    from collections import defaultdict
    
    answer = []
    report = list(set(report))
    user = defaultdict(set)
    cnt = defaultdict(int)
    
    for value in report:
        f,t = value.split()
        user[f].add(t)
        cnt[t] += 1
        
    for value in id_list:
        result = 0
        for u in user[value]:
            if cnt[u] >= k :
                result += 1
        answer.append(result)
    
    return answer