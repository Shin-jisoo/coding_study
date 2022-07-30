# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
import sys

S = sys.stdin.readline()

answer_list = [0, 0, 0, 0]

for i in S:
	if i == "1":
		answer_list[0] += 1
	if i == "I":
		answer_list[1] += 1
	if i == "l":
		answer_list[2] += 1
	if i == "|":
		answer_list[3] += 1
		
for i in answer_list:
	print(i)