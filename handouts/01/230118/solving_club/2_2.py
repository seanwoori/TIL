import sys
sys.stdin = open("input.txt", "r")

T = 10
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_num = input()
    org_mat = []
    n = 100

    for i in range(n):
        org_lst = list(map(int, input().split()))
        org_mat.append(org_lst)

    row_max = []
    
    raw_col_max = []
    col_max = []
    
    r_raw_dig_max = []
    l_raw_dig_max = []
    dig_max = []   
    
    for i in range(len(org_mat)):
        row_max.append(sum(org_mat[i]))

    for i in range(len(org_mat)):
        temp_col = []
        for j in range(len(org_mat)):
            temp_col.append(org_mat[j][i])
        raw_col_max.append(temp_col)
        r_raw_dig_max.append(org_mat[i][i])
        l_raw_dig_max.append(org_mat[-i-1][-i-1])

    for i in range(len(org_mat)):
        col_max.append(sum(raw_col_max[i]))
    
    dig_max.append(sum(r_raw_dig_max))
    dig_max.append(sum(l_raw_dig_max))
    
    max_val_lst = dig_max + col_max + row_max
    print(f'#{test_num} {max(max_val_lst)}')


    # ///////////////////////////////////////////////////////////////////////////////////