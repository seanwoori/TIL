import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for _ in range(T):
    lst = list(map(str, input()))

    ans = 2
    clst = list(set(lst))
    dct = {}

    for outc in clst:
        temp = []
        for idx, inc in enumerate(lst):
            if outc == inc:
                temp.append(idx)
        else:
            dct[outc] = temp
    print(dct)

    print(ans)