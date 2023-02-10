import sys
sys.stdin = open('input.txt', 'r')

def isRec(arr, n, k): # 입력 : arr와 arr 길이 n, 정사각형 길이 k
    a = []
    for i in range(n-k+1): # 큰 정사각형 세로 인덱스
        for j in range(n-k+1):  # 큰 정사각형 가로 인덱스
            temp = []
            for l in range(k): # 확인할 정사각형의 세로 인덱스
                temp.append(sum(arr[i+l][j:j+k]))
            a.append(sum(temp))
    return max(a)



T = int(input())
for tc in range(1,T+1):
    n, k = map(int, input().split())
    arr = [list(map(int, input().split())) for _ in range(n)]
    lst = []

    print(f'#{tc} {isRec(arr, n, k)}')