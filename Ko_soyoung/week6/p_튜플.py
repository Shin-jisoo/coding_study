def solution(s):
    result = []
    s = s[2:-2]
    s = s.split('},{')
    s.sort(key=len)
    arr = []
    for i in range(len(s)):
        if len(s[i]) > 1:
            arr.append(s[i].split(','))
        else:
            arr.append(s[i])

    for i in range(len(arr)):
        for j in range(len(arr[i])):
            if int(arr[i][j]) not in result:
                result.append(int(arr[i][j]))
    return result