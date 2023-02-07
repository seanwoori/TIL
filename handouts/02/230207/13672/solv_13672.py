import sys
sys.stdin = open('input.txt')

T = int(input())
for tc in range(1, T+1):
   n = int(input())
   di = [0, 1, 0, -1]
   dj = [1, 0, -1, 0]
   arr = [[0]*n for _ in range(n)]

   i=j=dr=0

   for cnt in range(1, n*n+1):
      arr[i][j] = cnt
      ni,nj = i+di[dr], j+dj[dr]
      if 0 <= ni <n and 0 <= nj < n and arr[ni][nj] == 0:
         i,j = ni,nj
      else:
         dr = (dr+1) % 4
         i,j = i+di[dr], j+dj[dr]

   print(f'#{tc}')
   for lst in arr:
      print(*lst)