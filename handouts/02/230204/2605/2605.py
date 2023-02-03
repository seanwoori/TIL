import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
lst = list(map(int, input().split()))


rnk = [i+1 for i in range(n)]
a = [] 

for i in range(n):
    a.insert(lst[i], rnk[i])

a = a[::-1]

for j in range(n):
    print(a[j], end=' ')