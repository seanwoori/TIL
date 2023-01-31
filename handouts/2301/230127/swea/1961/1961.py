import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    num_n = int(input())
    mat_lst = []

    for i in range(num_n):
        mat_lst.append(list(map(str, input().split())))
    
    def pi_half(mat):
        rslt_mat = []        
        for i in range(len(mat)):
            col_lst = []
            for j in range(len(mat)):
                col_lst.append(mat[len(mat)-1-j][i])
            rslt_mat.append(col_lst)
        return rslt_mat    

    def pi(mat):
        rslt_mat = []        
        for i in range(len(mat)):
            col_lst = []
            for j in range(len(mat)):
                col_lst.append(mat[len(mat)-1-i][len(mat)-1-j])
            rslt_mat.append(col_lst)
        return rslt_mat        

    def pi_one_half(mat):
        rslt_mat = []        
        for i in range(len(mat)):
            col_lst = []
            for j in range(len(mat)):
                col_lst.append(mat[j][len(mat)-1-i])
            rslt_mat.append(col_lst)
        return rslt_mat        
    
    def concat(*list):
        cc_mat = []
        for sub_lst in list:
            cc_mat.append(sub_lst)
        return cc_mat
    
    mat_concat = concat(pi_half(mat_lst), pi(mat_lst), pi_one_half(mat_lst))
    print(f'#{test_case}')
         
    for i in range(num_n):
        words = ''
        for j in range(len(mat_concat)):    
            words += ''.join(mat_concat[j][i]) + ' '
        print(words)   
    
    # ///////////////////////////////////////////////////////////////////////////////////