import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))
cache = []
m = 1

for i in range(len(lst)-1):
    if lst[i]>=lst[i+1]:
        m += 1
    else:
        cache.append(m)
        m=1
else:
    cache.append(m)

m = 1
for i in range(len(lst)-1):
    if lst[i]<=lst[i+1]:
        m+=1
    else:
        cache.append(m)
        m=1
else:
    cache.append(m)

print(max(cache))
