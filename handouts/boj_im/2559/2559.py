import sys
sys.stdin = open('input.txt', 'r')

n, k = map(int, input().split())
lst = list(map(int, input().split()))
ans = []
temp = 0
for l in range(k):
    temp += lst[l]
ans.append(temp)

for i,j in enumerate(range(k-1,len(lst)-1)):
    temp -= lst[i]
    temp += lst[j+1]
    ans.append(temp)

print(max(ans))