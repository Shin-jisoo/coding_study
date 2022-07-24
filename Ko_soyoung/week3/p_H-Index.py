def solution(citations):
    citations.sort()
    article_cnt = len(citations)

    for i in range(article_cnt):
        if citations[i] >= article_cnt - i:
            return article_cnt-i
    return 0