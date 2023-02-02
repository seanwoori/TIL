import sys
sys.stdin = open("sample_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    lst = list(map(int, input().split()))
    max_num, min_num = max(lst), min(lst)
    '''
    for i in range(N-1):
        for j in range(i+1, N):
            if lst[i] < lst[j]:
                if max_num < lst[j]:
                    max_num = lst[j]

            elif lst[i] > lst[j]:
                min_num = lst[j]
    '''
    ans = max_num - min_num

    print(f'#{test_case} {ans}')
    # ///////////////////////////////////////////////////////////////////////////////////
