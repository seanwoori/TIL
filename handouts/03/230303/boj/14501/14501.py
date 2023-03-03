import sys
sys.stdin = open('input.txt', 'r')

# 오늘부터 N+1 이 되는 날 퇴사
# 걸리는 시간 Ti, 받을 수 있는 금액 Pi

N=int(input())
lst=[list(map(int,input().split())) for _ in range(N)]

# 기대수익
for idx,lt in enumerate(lst):

    if lt[0]+(idx)<=len(lst)+1:
        pre = 0
        for i in range(lt[0]):
            pre+=lst[idx+i][1]

