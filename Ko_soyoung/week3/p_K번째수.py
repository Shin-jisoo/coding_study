def solution(array, commands):
    answer = []
    for i, j, k in commands:
        parse_array = sorted(array[i-1:j])
        answer.append(parse_array[k-1])
    return answer