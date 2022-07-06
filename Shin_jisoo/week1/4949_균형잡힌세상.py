while True:
    input_string = input()
    stack = []
    flag = 1
    
    if input_string == '.':
        break
    
    for value in input_string:
        if value == '(' or value == '[':
            stack.append(value)
            
        elif value == ')':
            if stack and stack[-1] == '(':
                stack.pop()
            else:
                flag = 0
                break
            
        elif value == ']':
            if stack and stack[-1] == '[':
                stack.pop()
            else:
                flag = 0
                break
            
    if flag and not stack:
        print("yes")
    else:
        print("no")