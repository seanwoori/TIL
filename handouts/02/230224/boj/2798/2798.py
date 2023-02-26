import sys
sys.stdin = open('input.txt', 'r')

N,M=map(int, input().split())       # N 카드의 갯수, M
lst=list(map(int, input().split()))
lst.sort(reverse=True)
mx=[]

for i in range(len(lst)):
    if lst[i]>=M:
        continue
    for j in range(i+1, len(lst)):
        for k in range(j+1, len(lst)):
            if lst[i]+lst[j]+lst[k]<=M:
                mx.append(lst[i]+lst[j]+lst[k])
print(max(mx))