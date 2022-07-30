# -*- coding: utf-8 -*-
# UTF-8 encoding when using korean
answer = 0
n,k = map(int, input().split())
students = []
for _ in range(n):
	s,y = map(int, input().split())
	students.append((s,y))

students.sort(key=lambda x:(x[0],x[1]))

tmp = (0,0)
cnt = 0
for student in students:
	if tmp == student:
		cnt += 1
		if cnt == k:
			answer += 1
			cnt = 0			
	else:
		answer += 1
		cnt = 0
	tmp = student
		

print(answer)