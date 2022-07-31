def solution(answers):
    person_1 = [1, 2, 3, 4, 5]
    person_2 = [2, 1, 2, 3, 2, 4, 2, 5]
    person_3 = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5]
    grade = [0, 0, 0]
    answer = []

    for i in range(len(answers)):
        if answers[i] == person_1[i % len(person_1)]:
            grade[0] += 1
        if answers[i] == person_2[i % len(person_2)]:
            grade[1] += 1
        if answers[i] == person_3[i % len(person_3)]:
            grade[2] += 1

    max_grade = max(grade)
    for i in range(len(grade)):
        if max_grade == grade[i]:
            answer.append(i+1)

    return answer