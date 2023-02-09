import sys
sys.stdin = open('input.txt', 'r')

garo, sero = map(int, input().split())
n = int(input()) # 북 : 1, 남 : 2, 서 : 3, 동 : 4
                 # 북 혹은 남에 위치한 경우 왼쪽으로부터의 거리
                 # 서 혹은 동에 위치한 경우 위쪽으로부터의 거리
                 # 마지막 줄에는 동근이의 위치
lst = list(list(map(int, input().split())) for _ in range(n+1))

a = [0] * (2*garo + 2*sero)



# 동근이의 위치가 기준점.
# 동근이가 북남, 혹은 동서에 따라 기준이 달라질듯?
# 리스트를 주욱 늘어뜨려볼까?
# 네모구조가 아니라, 2차원 리스트로 확인하면 되지 않을까?
# 리스트 크기는 2*garo + 2*sero
# 이후 동근이 좌표를 기준으로 잡으면?

print(lst)