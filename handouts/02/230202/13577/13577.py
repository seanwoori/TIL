import sys
sys.stdin = open("s_input.txt", "r")

T = int(input())
# 여러개의 테스트 케이스가 주어지므로, 각각을 처리합니다.
for test_case in range(1, T + 1):
    '''sol1
    lst = list(map(int, input()))
    lst.sort()

    ans = 0

    cnts = [0] * 10

    for n in lst:
        cnts[n] += 1

    i = 0

    while i <= 7:
        if cnts[i] >= 3:
            ans += 1
            cnts[i] -= 3
        else:
            i += 1

    i = 0
    while i <= 9:
        if cnts[i] >= 1 and cnts[i+1] >= 1 and cnts[i+2] >= 1:
            ans += 1
            cnts[i] -= 1
            cnts[i+1] -= 1
            cnts[i+2] -= 1
        else:
            i += 1
    '''
    '''sol2 while문을 통합한다면?
    리스트에 dummy [0]들을 2개 append
    '''
    '''
    빈도수를 판단하기 위해 등장하는 빈도수를 저장하는 리스트가 필요함.
    찾으면 한번 더, 없으면 그 다음 루프로 가야함.
    일차원 리스트로 2차원 정보를 나타낼 수 있구나.
    예를 들어, 위치값은 숫자 원소는 빈도수.
    '''
    '''
    def triplet(a):

        eig = list(set(a))
        flag = False

        for val1 in eig:
            if len(a) <= 2:
                break
            cnt = 0
            for val2 in a:
                if val2 == val1:
                    cnt += 1
            if cnt >= 3:
                flag = True
                a.remove(val1)
                a.remove(val1)
                a.remove(val1)


        return a, flag


    def run(a):

        eig = list(set(a))
        flag = False
        if len(eig) <= 2:
            return a, flag
        else:
            for i in range(1, len(eig)-1):
                if (eig[i+1] + eig[i-1]) == 2 * eig[i]:
                    flag = True

                    a.remove(eig[i-1])
                    a.remove(eig[i])
                    a.remove(eig[i+1])
            return a, flag


    print(run(lst)[1])
    #print(triplet(lst)[0], triplet(lst)[1])
    #print(run(lst)[0], run(lst)[1])
    #print(run(triplet(lst)[0])[0], run(triplet(lst)[0])[1])

    
    if ((run(lst)[1] == True) and (triplet(run(lst)[0])[1] == True)):
        rslt = 1
    elif ((triplet(lst)[1] == True) and (run(triplet(lst)[0])[1] == True)):
        rslt = 1
    '''
    print(f'#{test_case} {ans//2}')
