import sys
sys.stdin = open('input.txt', 'r')

garr = [list(map(int, input().split())) for _ in range(5)]
a = [list(map(int, input().split())) for _ in range(5)]
b =a[0]+a[1]+a[2]+a[3]+a[4]
def Bingo(arr): # 가로 세로 두 번 하기
    cnt = 0
    for i in range(5):
        if sum(arr[i]) == 5:
            cnt += 1
    return cnt
def diag_Bingo(arr): # 가로 인덱스 한번만
    cnt = 0
    temp1 = 0
    temp2 = 0
    for i in range(5):
        temp1 += arr[i][i]
        temp2 += arr[i][4-i]
    if temp1 == 5:
        cnt += 1
    if temp2 == 5:
        cnt += 1
    return cnt

def find_num(arr, num):
    for i in range(5):
        for j in range(5):
            if arr[i][j] == num:
                return i, j
k=0
while True:
    i, j = find_num(garr, b[k])
    garr[i][j]=1
    k+=1

    if k > 10:
        sarr = list(zip(*garr))
        if Bingo(garr)+Bingo(sarr)+diag_Bingo(garr) >= 3:
            print(k)
            break



