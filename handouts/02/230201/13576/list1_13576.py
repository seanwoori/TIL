import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())

for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    N = int(input())
    lst = list(map(int, input().split()))
    ans = 0

    def getMax(list):
        rslt = 0
        for num in list:
            if rslt < num:
                rslt = num
        return rslt

    def getMin(list):
        rslt = 10000000
        for num in list:
            if rslt > num:
                rslt = num
        return rslt

    ans = getMax(lst) - getMin(lst)
    print(f'#{test_case} {ans}')
    # ///////////////////////////////////////////////////////////////////////////////////
