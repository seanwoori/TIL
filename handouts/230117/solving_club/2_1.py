import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_num = int(input())
    lst_a = list(map(int, input().split()))
    lst_a.sort()
    unq_lst = list(set(lst_a))
    count_lst = []
    
    for char_1 in unq_lst:
        count_num = 0
        for char_2 in lst_a:
            if char_1 == char_2:
                count_num += 1
        count_lst.append(count_num)

    dict_ans = dict(zip(unq_lst, count_lst))
    sort_ans = sorted(dict_ans.items(), key = lambda x : x[1])
    print(f'#{test_num} {sort_ans[-1][0]}')

