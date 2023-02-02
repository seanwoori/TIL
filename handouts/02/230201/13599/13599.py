import sys
sys.stdin = open("s_input.txt", "r")

T = 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    lst = list(map(int, input().split()))

    rslt = 0

    for i in range(2):
        temp_lst = []
        if i == 0:
            for j in range(0, 3):
                temp_lst.append(lst[j])
            if lst[i] == max(temp_lst):
                temp = temp_lst.pop(0)
                rslt += temp - max(temp_lst)

        if i == 1:
            for j in range(0, 4):
                temp_lst.append(lst[j])
            if lst[i] == max(temp_lst):
                temp = temp_lst.pop(1)
                rslt += temp - max(temp_lst)

    for i in range(n-2, n):
        temp_lst = []
        if i == (n-2):
            for j in range(n-4, n):
                temp_lst.append(lst[j])
            if lst[i] == max(temp_lst):
                temp = temp_lst.pop(n-2)
                rslt += temp - max(temp_lst)

        if i == (n-1):
            for j in range(n-3, n):
                temp_lst.append(lst[j])
            if lst[i] == max(temp_lst):
                temp = temp_lst.pop(n-1)
                rslt += temp - max(temp_lst)


    for i in range(2, n-2):
        temp_lst = []
        for j in range(i-2, i+3):
            temp_lst.append(lst[j])
        if lst[i] == max(temp_lst):
            temp = temp_lst.pop(2)
            rslt += temp - max(temp_lst)

    print(f'#{test_case} {rslt}')

    # ///////////////////////////////////////////////////////////////////////////////////