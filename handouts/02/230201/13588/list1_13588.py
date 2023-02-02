import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n_num, m = map(int, input().split())
    lst = list(map(int, input().split()))

    def partSum(list, n, m):
        rslt = []

        for i in range(n-m+1):
            temp_sm = 0
            for j in range(i, i+m):
                temp_sm += list[j]
            rslt.append(temp_sm)

        return rslt

    print(f'#{test_case} {max(partSum(lst, n_num, m)) - min(partSum(lst, n_num, m))}')
    # ///////////////////////////////////////////////////////////////////////////////////