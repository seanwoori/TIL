import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    # 10개의 달란트를 모은 원생에게 10개의 사탕을 주는 것이 아니라,
    # 10개를 3묶음으로 나누어서 각 묶음의 곱의 개수로 사탕을 교환
    N,P=map(int, input().split())


    if N%P:
        ans=(N//P)**(P-(N%P))
        for i in range(N%P):
            ans*=(N//P+1)
    else:
        ans=(N//P)**P

    print(f'#{tc} {ans}')