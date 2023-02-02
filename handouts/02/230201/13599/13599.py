import sys
sys.stdin = open("s_input.txt", "r")

T = 3
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    # ///////////////////////////////////////////////////////////////////////////////////
    n = int(input())
    lst = list(map(int, input().split()))
    '''
    좌/우 2칸, 나를 제외 최대값 
    나는 문제 조건에 초기 좌/우 2칸에 0이 append 되어있다고 생각하지 못함. 
    즉, 문제를 잘 읽지 않고 바로 코딩으로 들어가 이러한 문제가 야기됨.
    
    때문에 처음과 나중 둘을 예외로 삼아 다루려고함.
    그러다보니, 예외케이스에 대한 for문이 너무 많이 들어감.
    교수님처럼 0을 본 리스트에 append 한다면, 코드가 매우 간결해질 것으로 생각함.
    하단은 예외처리를 위해 작성한 for loop들.
    
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
    '''

    rslt = 0

    for i in range(2, n-2):
        temp_lst = []
        for j in range(i-2, i+3):
            temp_lst.append(lst[j])
        if lst[i] == max(temp_lst):
            temp = temp_lst.pop(2)
            rslt += temp - max(temp_lst)

    print(f'#{test_case} {rslt}')


    # ///////////////////////////////////////////////////////////////////////////////////