def solution(sizes):
    width = 0
    height = 0
    for w, h in sizes:
        if w > h:
            w, h = h, w
        width = max(width, w)
        height = max(height, h)
    return width * height