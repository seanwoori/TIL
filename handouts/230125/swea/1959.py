import sys
sys.stdin = open("input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T+1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n, m = map(int, input().split())

    n_lst = list(map(int, input().split()))
    m_lst = list(map(int, input().split()))

    sum_val_lst = []
    

    if n >= m:
        n_lst, m_lst = m_lst, n_lst
    else:
        pass

    for i in range(len(n_lst)):
                
        if i > (len(m_lst) - len(n_lst)):       
            break
        else:
            new_val_n_lst = n_lst
            new_val_m_lst = m_lst[i:(i+n)]
            
            #print(new_val_n_lst)
            #print(new_val_m_lst)
            sum_val = 0
            for i in range(len(new_val_n_lst)):        
                sum_val += new_val_n_lst[i] * new_val_m_lst[i]
            sum_val_lst.append(sum_val)

    print(f'#{test_case} {max(sum_val_lst)}')        
    # ///////////////////////////////////////////////////////////////////////////////////
