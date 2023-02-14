import sys
sys.stdin = open('input.txt', 'r')

k = int(input())
di = [0, 0, 1, -1] # x축 0:동,  1:서, 2:남, 3:북
dj = [1, -1, 0, 0]
arr = list([0]*500 for _ in range(500))
dr = 0
for _ in range(6):
    m, n = list(map(int, input().split()))
    dr=m-1
    if m==1:
        for i in range(n):
            i=
            arr[n]
    else:
        arr[m-1] = n

for i,nu in enumerate(arr):
    if type(nu)==int and i==0 or i==1:
        garo = nu
    elif type(nu)==int and i==1 or i==1

area = mx-mn
print(k*area)