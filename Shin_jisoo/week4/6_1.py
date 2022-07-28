#다음과 같이 import를 사용할 수 있습니다.
#import math
import queue

def solution(n, garden):
    #여기에 코드를 작성해주세요.
    answer = 0
    q = queue.Queue()
    dx,dy = [0,-1,0,1],[1,0,-1,0]
    
    for i in range(n):
        for j in range(n):
            if garden[i][j] == 1:
                q.put((i,j,0))
                
    while q.empty() == False:
        x, y, day = q.get()
        for i in range(4):
            nx,ny = x+dx[i], y+dy[i]
            next_day = day+1
            if 0<=nx<n and 0<=ny<n:
                if garden[nx][ny] == 0:
                    garden[nx][ny] = 1
                    answer = next_day
                    q.put((nx,ny,next_day))
        
    return answer

#아래는 테스트케이스 출력을 해보기 위한 코드입니다.
n1 = 3
garden1 = [[0, 0, 0], [0, 1, 0], [0, 0, 0]]
ret1 = solution(n1, garden1)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret1, "입니다.")

n2 = 2
garden2 = [[1, 1], [1, 1]]
ret2 = solution(n2, garden2)

#[실행] 버튼을 누르면 출력 값을 볼 수 있습니다.
print("solution 함수의 반환 값은", ret2, "입니다.")