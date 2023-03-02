import sys
import copy

def cnt(arr):
    cnt=1
    temp=[]
    for i in range(N):
        for j in range(N-1):
            if arr[i][j]==arr[i][j+1]:
                cnt+=1
            else:
                temp.append(cnt)
                cnt=1
        else:
            temp.append(cnt)
            cnt=1
    return max(temp)

def switch(arr):
    a=[]
    for ci in range(N):
        for cj in range(N):
            for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
                ni, nj = ci + di, cj + dj
                if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] != arr[ni][nj]:
                    temp = copy.deepcopy(arr)
                    temp[ci][cj], temp[ni][nj] = temp[ni][nj], temp[ci][cj]
                    stemp=list(zip(*temp))
                    a.append(max([cnt(temp), cnt(stemp)]))
    return max(a)

sys.stdin = open('input.txt', 'r')
input=sys.stdin.readline

# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
N=int(input())
garr=list(list(map(str, input())) for _ in range(N))
ans=switch(garr)
print(ans)