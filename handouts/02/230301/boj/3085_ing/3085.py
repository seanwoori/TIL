import sys
import copy

def cnt(arr):
    atemp=[0]
    idx=[]
    for i in range(N):
        ans = 1
        for j in range(N - 1):
            if arr[i][j]==arr[i][j+1]:
                ans+=1
            else:
                if ans>=max(atemp):
                    atemp.append(ans)
                    idx.append([i,j])
                ans = 1
        else:
            if ans >= max(atemp):
                atemp.append(ans)
                idx.append([i,j])
    return max(atemp), idx

def switch(arr, ci,cj):
    a=[]
    for di, dj in [(0, 1), (0, -1), (1, 0), (-1, 0)]:
        ni, nj = ci + di, cj + dj
        if 0 <= ni < N and 0 <= nj < N and arr[ci][cj] != arr[ni][nj]:
            temp = copy.deepcopy(arr)
            temp[ci][cj], temp[ni][nj] = temp[ni][nj], temp[ci][cj]
            stemp=list(zip(*temp))
            a.append(max([cnt(temp)[0], cnt(stemp)[0]]))
    return max(a)


sys.stdin = open('input.txt', 'r')

# 빨간색은 C, 파란색은 P, 초록색은 Z, 노란색은 Y
#
N=int(input())
garr=list(list(map(str, input())) for _ in range(N))
sarr=list(zip(*garr))

mx=max([cnt(garr)[0],cnt(sarr)[0]])

if mx==cnt(garr)[0]:
    ans=[]
    for lst in cnt(garr)[1]:
        ci,cj=lst[0],lst[1]
        ans.append(switch(garr,ci,cj))
else:
    ans = []
    for lst in cnt(sarr)[1]:
        ci, cj = lst[0], lst[1]
        ans.append(switch(sarr, ci, cj))

print(max(ans))