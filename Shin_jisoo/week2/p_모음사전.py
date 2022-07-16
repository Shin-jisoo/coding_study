def solution(word):
    from itertools import product
    answer = 0
    
    words = []
    
    for i in range(1,6):
        for c in product(['A','E','I','O','U'], repeat=i):
            words.append(''.join(list(c)))

    
    words.sort()
    answer = words.index(word)+1
                         
    return answer