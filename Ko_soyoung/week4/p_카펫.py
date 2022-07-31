def solution(brown, yellow):
    answer = []
    yellow_x = 0
    yellow_y = 0

    for i in range(1, yellow + 1):
        if yellow % i == 0:
            yellow_x = int(yellow / i)
            yellow_y = i
            if yellow_x * 2 + yellow_y * 2 + 4 == brown:
                answer.append(yellow_x + 2)
                answer.append(yellow_y + 2)
                return sorted(answer, reverse=True)
    return answer




print(solution(10, 2)) #[4, 3]
print(solution(8, 1)) #[3, 3]
print(solution(24, 24)) #[8, 6]