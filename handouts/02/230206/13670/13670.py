import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, T+1):
    # 이진수로 풀면 빠르게 풀 수 있음.
    lst = list(map(int, input().split()))
    n = len(lst)
    ans = 0

    # 공집합을 제외한 모든 조합을 비트로 표시.
    # bit를 flag라고 여길 수 있음.
    for bit in range(1, 1<<n):
        sm = 0
        # bit 0의 자리부터 bit n-1까지 한자리씩 flag를 체크.
        for i in range(n):
            if bit & (1<<i): # 해당 비트가 0이 아니면,
                sm += lst[i]
        if sm == 0:
            ans = 1
            break

    print(f'#{tc} {ans}')