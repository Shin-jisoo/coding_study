def solution(s):
    stack = []
    if len(s) % 2 or s[0] == ")" or s[-1] == "(":
        return False

    for i in s:
        if len(stack) == 0:
            if i == ")":
                return False
            else:
                stack.append(i)
        else:
            if i == "(":
                stack.append(i)
            else:
                if stack[-1] != i:
                    stack.pop()
                else:
                    stack.append(i) 
    return len(stack) == 0