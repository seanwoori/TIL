import sys
sys.stdin = open('input.txt', 'r')

N,M,L=map(int, input().split())
lst=[0]*N
idx=0 # idx+1은 현재위치
cnt=0
# 한 사람이 공을 M번 받았으면 게임은 끝
# 공을 받은 횟수가 홀수번이면 자기의 현재 위치에서 시계방향으로 L번째 있는 사람에게
# 짝수번이면 현재 위치에서 반시계 방향으로 L번째 있는 사람에게
while True:
    lst[idx] += 1
    if lst[idx]==M:
        break
    if lst[idx]%2: # 홀수번이면
        idx=(idx+L)%(N)
        cnt+=1
    else:          # 짝수번이면
        idx=(idx-L)%(N)
        cnt+=1
print(cnt)