def solution(s):
    stack = []
    stack.append(s[0])
    for i in range(1, len(s)):
        if len(stack) == 0:
            stack.append(s[i])
        else:
            word = stack.pop()
            if word != s[i]:
                stack.append(word)
                stack.append(s[i])

    if len(stack) == 0:
        answer = 1
    else:
        answer = 0
    return answer