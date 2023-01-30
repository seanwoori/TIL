import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    mat_lst = []
    '''
    if test_case == 1:
        pass
    else:
        continue
    '''
    for i in range(9):
        mat_lst.append(list(map(int, input().split())))

    def factorial(n):
        result = 1
        for i in range(1, 1+n):
            result *= i
        return result

    
    def row(mat):
        for lst in mat:
            cert = 1
            for i in range(len(lst)):
                cert *= lst[i]
            if cert == factorial(9):
                return True
            else:
                return False

    def col(mat):
        for i in range(len(mat)):
            cert = 1
            for j in range(len(mat)):
                cert *= mat[j][i]
            if cert == factorial(9):
                return True
            else:
                return False

    def nine(mat):
        cert = 1
        temp_mat = []
        for i in range(3):                
            temp_mat.append(mat.pop(0))        
            for j in range(3):
                cert *= temp_mat[i].pop(0)
        if cert == factorial(9):
            return True
        else:
            return False 
    
    flag = False
    if (row(mat_lst) == True) and (col(mat_lst) == True) and (nine(mat_lst) == True):
        flag = True

    print(f'#{test_case} {flag}')
    

    # ///////////////////////////////////////////////////////////////////////////////////
