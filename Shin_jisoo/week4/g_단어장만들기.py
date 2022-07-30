# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
n,k = map(int, input().split())
words = []
for _ in range(n):
	words.append(input())
	
words.sort(key=lambda x: (len(x),x))

print(words[k-1])