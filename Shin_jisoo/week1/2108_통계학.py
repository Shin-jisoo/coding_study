import sys
from collections import Counter

num = []
cnt = int(sys.stdin.readline())
for _ in range(cnt):
    num.append(int(sys.stdin.readline()))
    
#산술평균
#n개의 수들의 합을 n으로 나눈 값
sum = 0
for value in num:
    sum = sum + value
    
print(round(sum/cnt))

#중앙값
#n개의 수들을 증가하는 순서로 나열했을 경우 그 중앙에 위치하는 값
num.sort()
middle = int(cnt/2)
print(num[middle])

#최빈값
#n개의 수들 중 가장 많이 나타나는 값
dic = Counter(num)
modes = dic.most_common()

if cnt > 1:
    if modes[0][1] == modes[1][1]:
        print(modes[1][0])
    else:
        print(modes[0][0])
else:
    print(modes[0][0])
    
#범위
#n개의 수들 중 최댓값과 최솟값의 차이
max_num = num[-1]
min_num = num[0]
print(max_num - min_num)