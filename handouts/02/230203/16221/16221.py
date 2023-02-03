import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for test_case in range(1, T+1):
    d, a, b, f = map(int, input().split())
    '''
    d = 250
    a = 10
    b = 15
    f = 20
    각 항에 줄어드는 거리 계산 필요함.
    각 항의 소요시간에 대해 규칙성이 있을 것임.
    35 30 35 30 35 30
    '''
    '''
    ab, fa, fb = a+b, f+a, f+b

    def DRemain(vel, d):
        t = d / vel
        rem = t * ab
        d = d - rem
        ans = t * f
        return d, ans

    ans = 0

    while True:
        a, b = DRemain(fa, d)
        d = a
        ans += b
        a, b = DRemain(fb, d)
        d = a
        ans += b
        if d <= 1e-10:
            break
    '''
    ans = d / (a + b) * f
    print(f'#{test_case} {ans}')