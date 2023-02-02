import sys

sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    tk, fin, nbt = map(int, input().split())
    nbt_lst = [0] + list(map(int, input().split()))

    if test_case == 3:
        pass
    else:
        continue

    cnt = 0
    temp_idx1 = 0
    temp_idx2 = temp_idx1 + 2
    flag = False


    while True:

        if nbt_lst[temp_idx1] + tk < nbt_lst[temp_idx1 + 1]:
            flag = True
            break

        if nbt_lst[temp_idx1] + tk >= fin:
            if temp_idx1 == len(nbt_lst) - 2:
                if nbt_lst[temp_idx1] + tk >= nbt_lst[temp_idx1 + 1]:
                    temp_idx1 += 1
                    cnt += 1
                    break

        if temp_idx2 == len(nbt_lst) - 2:
            temp_idx1 += 1
            temp_idx2 = temp_idx1 + 2
            continue

        print(temp_idx1, temp_idx2)

        if nbt_lst[temp_idx1] + tk >= nbt_lst[temp_idx2]:
            cnt += 1
            temp_idx2 += 1
            continue

        else:
            temp_idx1 += 1
            temp_idx2 = temp_idx1 + 2
            continue

        print(cnt)

    if flag == True:
        ans = 0
    else:
        ans = nbt - cnt
    
    print(f'#{test_case} {ans}')
