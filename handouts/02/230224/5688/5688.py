import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
# 이진탐색을 통해 세제곱근 빠르게 구할 수 있음
# 혹은 세제곱근 구하는 공식을 이용하여
for tc in range(1, 1+T):
    N=int(input())
    s,e=1,N
    ans=-1
    while s<=e:
        m=(s+e)//2
        if m**3==N:
            ans=m
            break
        elif m**3<N:
            s=m+1
        elif m**3>N:
            e=m-1

    print(f'#{tc} {ans}')
