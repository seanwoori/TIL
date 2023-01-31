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
    #print(mat_lst)

    def factorial(n):
        result = 1
        for i in range(1, 1+n):
            result *= i
        return result

    
    def row(mat):
        flag = True
        for lst in mat:
            cert = 1
            for i in range(len(lst)):
                cert *= lst[i]
            if cert == factorial(9):
                flag = True
            else:
                flag = False
                break
        return flag
    
    def col(mat):
        flag = False
        for i in range(len(mat)):
            cert = 1
            for j in range(len(mat)):
                cert *= mat[j][i]
            if cert == factorial(9):
                flag = True
            else:
                flag = False
                break
        return flag


    #print(mat_lst)

    def nine(mat):
        flag = True
        temp_mat = []
        for_loop = True

        for m in range(3):
            temp_mat = []
            for i in range(3):                
            
                temp_mat.append(mat.pop(0))        
            
                if i == 2 or i == 5 or i == 8:
                    for j in range(3):
                        cert = 1
                        for k in range(3):
                            for l in range(3):
                                cert *= temp_mat[k].pop(0)
                        #print(cert)
                        #print(temp_mat)
                        if cert == factorial(9):
                            flag = True
                        else:
                            flag = False
                            for_loop = False
                            break
                    if for_loop == False:
                        break
                if for_loop == False:
                    break
            if for_loop == False:
                break
        return flag
                         
    flag_ovr = 0
    
    if (row(mat_lst) == True) and (col(mat_lst) == True) and (nine(mat_lst) == True):
        flag_ovr = 1

    print(f'#{test_case} {flag_ovr}')
    

    # ///////////////////////////////////////////////////////////////////////////////////
