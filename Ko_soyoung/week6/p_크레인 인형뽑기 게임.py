def solution(board, moves):
    stack = []
    result = 0
    while len(moves) > 0:
        crane = moves.pop(0)
        for i in range(len(board)):
            if board[i][crane-1] != 0:
                if stack:
                    if stack[-1] == board[i][crane-1]:
                        stack.pop()
                        result += 2
                        board[i][crane - 1] = 0
                        break
                stack.append(board[i][crane-1])
                board[i][crane - 1] = 0
                break
    return result