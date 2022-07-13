def solution(answers):
    answer = []
    a = [1,2,3,4,5]
    b = [2,1,2,3,2,4,2,5]
    c = [3,3,1,1,2,2,4,4,5,5]
    
    c1,c2,c3 = 0,0,0
    
    for i,v in enumerate(answers):
        first = a[i%5]
        second = b[i%8]
        third = c[i%10]
        
        if first == v:
            c1 += 1
        if second == v:
            c2 += 1
        if third == v:
            c3 += 1
            
    max_cnt = max(c1,c2,c3)
    if max_cnt == c1:
        answer.append(1)
    if max_cnt == c2:
        answer.append(2)
    if max_cnt == c3:
        answer.append(3)
    
    return answer