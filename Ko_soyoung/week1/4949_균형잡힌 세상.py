while True:
    words = input()
    stack = []

    if words == ".":
        break

    for w in words:
        if w == "(" or w == "[":
            stack.append(w)
        elif w == ")":
            if len(stack) and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(w)
        elif w == "]":
            if len(stack) and stack[-1] == "[":
                stack.pop()
            else:
                stack.append(w)

    if len(stack) == 0:
        print("yes")
    else:
        print("no")