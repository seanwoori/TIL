import sys
sys.stdin = open('input.txt', 'r')

'''
def isFit(arr,n,k): # n=가로,세로 길이 / k=단어의 길이
    cnt = 0
    for i in range(n): # 가로 전부 탐색
        for num in arr[i]:
            if num == 0:
                cnt += 1
        if c
'''

T = int(input())
for tc in range(1, 1+T):
    n, k = map(int, input().split()) # n = 가로, 세로 길이 / k = 단어의 길이

    arr_g = [list(map(int, input().split())) for _ in range(n)]
    arr_s = list(zip(*arr_g))

    if tc == 1:
        pass
    else:
        continue

