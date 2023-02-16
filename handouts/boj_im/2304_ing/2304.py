import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
lst = [list(map(int, input().split())) for _ in range(T)]
lst.sort(key=lambda x:x[0])
mxidx=mx=0
flag = False
for idx, lt in enumerate(lst):
    if mx<lt[1]:
        mx=lt[1]
        mxidx=idx
    elif mx==lt[1]:
        flag = True

print(mxidx)


print(lst)