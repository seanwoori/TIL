import sys
sys.stdin = open('input.txt', 'r')


T = int(input())
for tc in range(1, 1+T):
    st1 = str(input())
    st2 = str(input())

    m, n = len(st1), len(st2)
    ans = 0
    if st1 in st2:
        ans = 1


    print(f'#{tc} {ans}')