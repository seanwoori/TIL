import sys
sys.stdin = open("input_2_2.txt", "r")

# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, 10 + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    test_num = int(input())
    nrows = 100
    ncols = 100

    origin_lst = list(map(int, input().split()))
    origin_mat = []
    print(origin_lst)

    for i in range(nrows):
        row_mat = []
        for j in range(ncols*nrows, ncols*nrows + 100):
            if ncols*nrows == 10000:
                break
            row_mat.append(origin_lst[j])
        origin_mat.append(row_mat)
    

    print(origin_mat)

    
        
    # ///////////////////////////////////////////////////////////////////////////////////