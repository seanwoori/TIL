import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n = int(input())
    lst = list(map(int, input().split()))
    lst = list(dict.fromkeys(lst)) # 중복 원소 거르기
    up = sorted(lst) #비교 리스트 생성


    def isinup(list): # 비교대상 리스트 입력
        idx = up.index(list[0])
        temp1 = up[idx:len(list)]
        if temp1 == list:
            return True
        else:
            return False

    ans_lst = []

    for i in range(n-1): # 리스트 인덱스에 따른 원소 추적
        temp = []
        for j in range(i, n):
            temp.append(lst[i:j+1])
        for b in temp:
            if isinup(b) == True:
                ans_lst.append(len(b))
    else:
        if ans_lst == []:
            ans_lst.append(1)

    print(f'#{test_case} {max(ans_lst)}')
