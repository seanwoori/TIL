import sys
sys.stdin = open('input.txt', 'r')

# 가로방향이 오목인 함수 작성
def garoOmok(arr):
    for lst in arr:
        cnt=0
        for ch in lst:
            if ch=='o':
                cnt+=1
                if cnt>=5:
                    return True
            else:
                cnt=0
    return False
# 대각선 방향이 오목인 함수 작성
def diagOmok1(arr):
    for k in range(N-4):
        for l in range(N-4):
            cnt=0
            # cnt는 루프 돌기 전에 초기화
            for i in range(5):
                if arr[k+i][l+i]=='o':
                    cnt+=1
                    if cnt>=5:
                        return True
                else:
                    cnt=0
    return False

def diagOmok2(arr):
    for k in range(N-4):
        for l in range(N-4):
            cnt = 0
            for i in range(5):
                if arr[k+i][l+4-i]=='o':
                    cnt+=1
                    if cnt>=5:
                        return True
                else:
                    cnt=0
    return False

T = int(input())

for tc in range(1, 1+T):
    N = int(input())
    garr = [list(input()) for _ in range(N)]
    # print(garr)
    # 오목 판정 문제
    # 가로세로는 arr.T 로 판정가능.
    # 대각선은 [i][j], [i][4-j]로 판정.

    sarr = list(map(list, zip(*garr)))
    #print(sarr)

    if garoOmok(garr) or garoOmok(sarr) or diagOmok1(garr) or diagOmok2(garr):
        ans = 'YES'
    else:
        ans='NO'

    print(f'#{tc} {ans}')