T = int(input())
for tc in range(1, T + 1):
    N = int(input()) // 10
    lst = [1, 3]
    for i in range(2, N):
        lst.append(lst[i - 2] * 2 + lst[i - 1])
 
    print(f'#{tc}', lst[-1])
