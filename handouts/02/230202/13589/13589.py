import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    lst = list(map(int, input()))
    cnts = [0] * 10

    for n in lst:
        cnts[n] += 1

    print(f'#{test_case} {max} {min}')
    # ///////////////////////////////////////////////////////////////////////////////////
