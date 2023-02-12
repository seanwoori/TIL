import sys
sys.stdin = open('input.txt', 'r')
# 최대 수?
n = int(input())
mx = 0
ans = []

for i in range(1,n+1)[::-1]:
    lst = [n]
    lst.append(i)
    for j in range(1,30000):
        if lst[j-1]-lst[j] >= 0:
            lst.append(lst[j-1]-lst[j])
        else:
            break

    if mx < len(lst):
        mx = len(lst)
        ans = lst

print(mx)
print(*ans)