import sys
sys.stdin = open('input.txt', 'r')


a = list(map(int, input().split()))
ac = [i+1 for i in range(8)]
dc = [i+1 for i in range(8)[::-1]]
ans = ''

if a == ac:
    ans = 'ascending'
elif a == dc:
    ans = 'descending'
else:
    ans = 'mixed'

print(ans)