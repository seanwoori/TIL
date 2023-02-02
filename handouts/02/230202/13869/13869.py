import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
   n = int(input())
   lst = list(map(int, input().split()))
   eig = list(set(lst))


   cnt = [0] * 101
   ans = [0] * len(lst)

   for n in lst:
       cnt[n] += 1

   for i in range(1, len(cnt)):
       cnt[i] += cnt[i-1]

   for i in lst:
       cnt[i] -= 1
       ans[cnt[i]] = i

   print(f'#{test_case}', *ans)