def dfs(i, N, s, K):
    global cnt
    if s > K:
        return
    elif s == K:
        if sum(bit) == N:
            cnt += 1
        return
    elif i > 11:
        return
    else:
        bit[i] = 1
        dfs(i + 1, N, s + lst[i], K)
        bit[i] = 0
        dfs(i + 1, N, s, K)


T = int(input())

for tc in range(1, 1 + T):
    N, K = map(int, input().split())
    lst = [i for i in range(1, 13)]
    cnt = 0
    bit = [0] * 12

    dfs(0, N, 0, K)
    print(f'#{tc} {cnt}')