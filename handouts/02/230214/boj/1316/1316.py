import sys
sys.stdin = open('input.txt', 'r')

n = int(input())
ans = 0
for _ in range(n):
    wrd = input()
    err = 0
    for idx in range(len(wrd)-1):
        if wrd[idx] != wrd[idx+1]:
            nwrd = wrd[idx+1:]
            if nwrd.count(wrd[idx]) > 0:
                err += 1
    if err == 0:
        ans += 1
print(ans)
