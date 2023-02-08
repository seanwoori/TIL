import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    _, n = map(str, input().split())
    n = int(n)
    inp = list(map(str, input().split()))

    dct = {"ZRO":0, "ONE":1, "TWO":2, "THR":3, "FOR":4, "FIV":5, "SIX":6, "SVN":7, "EGT":8, "NIN":9}
    rv_dct = dict(map(reversed, dct.items()))
    slst = []
    ans = []

    for ch in inp:
        slst.append(dct[ch])
    slst.sort()


    for num in slst:
        ans.append(rv_dct[num])

    print(f'#{tc}')
    print(*ans)