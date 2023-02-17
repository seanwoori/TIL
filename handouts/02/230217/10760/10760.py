import sys
sys.stdin = open('input.txt', 'r')

# 최적의 상륙 지저을 정하고자 함
# 8개의 방향 중 사진을 찍을 수 있는 방향이 4방향 이상인 지점으로 정하고자 함.
# 예비 후보지의 수를 알아내는 프로그램 작성하여라.
T = int(input())
for tc in range(1, 1+T):
    sero, garo = map(int, input().split())
    arr = [[0]*(garo+2)] + [[0]+list(map(int, input().split()))+[0] for _ in range(sero)] + [[0]*(garo+2)]
    # 8방향을 볼 수 있는 범위를 i와 j를 통해 확인함.
    cnt = 0
    for i in range(1, sero+1):
        for j in range(1, garo+1):
            temp = 0
            for k in range(i-1, i+2):
                for l in range(j-1, j+2):
                    if arr[i][j]>arr[k][l]>0:
                        temp += 1

            if temp >= 4:
                cnt+=1

    print(f'#{tc} {cnt}')