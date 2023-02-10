import sys
sys.stdin = open('input.txt', 'r')

sero, garo  = map(int, input().split())

def isGuard(arr):
    cnt = 0
    for i in range(len(arr)):
        if 'X' in arr[i]:
           cnt += 1
    return len(arr)-cnt

sarr = [list(map(str, input())) for _ in range(sero)]
garr = list(map(list, zip(*sarr)))
print(max(isGuard(sarr), isGuard(garr)))
