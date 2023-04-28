from collections import deque
# 문제의 경우 1은 시계방향, -1은 반시계 방향이다.
# deque의 rotate = -1일 경우 반시계 방향, 1일 경우 시계 방향으로 움직인다.

def check_right(start, dirs):
    # 더 이상 조사가 불가능한 경우
    if start > 3 or gears[start-1][2] == gears[start][6]:
        return

    # 오른쪽 확인
    if gears[start-1][2] != gears[start][6]:
        # 인접한 톱니바퀴가 회전 가능한지부터 먼저 파악한다.
        check_right(start + 1, -dirs)
        # 회전시킨다.
        gears[start].rotate(dirs)


def check_left(start, dirs):
    if start < 0 or gears[start][2] == gears[start+1][6]:
        return
    
    # 왼쪽 확인
    if gears[start+1][6] != gears[start][2]:
        check_left(start - 1, -dirs)
        gears[start].rotate(dirs)
        

gears = [input() for _ in range(4)]
n = int(input())

for _ in range(n):
    num, dirs = map(int, input())

    # 기준 톱니바퀴가 주어졌을 때, 오른쪽 / 왼쪽이 회전 가능한지를 각각 확인하고 회전시킨다.
    check_right(num+1, -dirs)
    check_left(num-1, -dirs)
    # 기준 톱니바퀴를 회전시킨다.
    gears[num].rotate(dirs)
    

result = 0
for i in range(4):
    result += (2**i) * gears[i+1][0]
print(result)