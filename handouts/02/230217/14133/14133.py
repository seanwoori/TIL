def play(arr):
    # print("play 시작")
    # 좌상, 좌하, 우상, 우하, 좌, 우, 상, 하 : 8방
    direction = [(-1, -1), (-1, 1), (1, 1), (1, -1), (-1, 0), (1, 0), (0, 1), (0, -1)]
    now = (arr[0], arr[1])  # 현재 위치
    # visited = [[0] * n for _ in range(n)]
    if arr[2] % 2:  # player에 따라 상대방 돌 정하기
        opponent = 2
    else:
        opponent = 1
    # opponent = (arr[2] % 2) + 1

    for d in direction:
        nx, ny = now[0] + d[0], now[1] + d[1]
        if nx >= n or nx < 0 or ny >= n or ny < 0:
            # print("play에서 테이블 밖으로 나감")
            continue
        else:
            if table[ny][nx] == opponent:
                # print("play에서 상대 돌 찾음")
                # stack.append((nx, ny))
                # visited[ny][nx] = 1
                next_v = (nx, ny)
                road_to_flip(arr, d, next_v, opponent)
            else:
                # print("play 상대 돌 못찾음")
                continue
    table[arr[1]][arr[0]] = arr[2]


def road_to_flip(arr, d, start, opponent):
    road = [start]  # 왔던 길 flip하기 위한 리스트
    while True:
        nx, ny = road[-1][0] + d[0], road[-1][1] + d[1]
        if nx >= n or nx < 0 or ny >= n or ny < 0 or table[ny][nx] == 0:

            return
        else:
            if table[ny][nx] == opponent:
                road.append((nx, ny))

            else:
                for flip in road:
                    table[flip[1]][flip[0]] = arr[2]
                # print("flip 끝")
                return


t = int(input())
for tc in range(1, t + 1):
    n, game_count = map(int, input().split())  # n*n 행렬, 라운드 진행 횟수

    table = [[0] * n for _ in range(n)]
    table[n // 2][n // 2] = 2
    table[n // 2 - 1][n // 2 - 1] = 2
    table[n // 2 - 1][n // 2] = 1
    table[n // 2][n // 2 - 1] = 1
    # pprint.pprint(table)

    games = []
    for idx in range(game_count):
        games.append(list(map(int, input().split())))
        games[idx][0] -= 1
        games[idx][1] -= 1

    for game in games:
        play(game)

    black = 0
    white = 0
    for i in range(n):
        black += table[i].count(1)
        white += table[i].count(2)

    print(f"#{tc} {black} {white}")