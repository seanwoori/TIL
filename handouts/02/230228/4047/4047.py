import sys
sys.stdin = open('input.txt', 'r')

dct={'S':0, 'D':1, 'H':2, 'C':3}

T = int(input())
for tc in range(1, 1+T):
    '''
    영준이의 카드 카운팅
    스페이드, 다이아, 하트, 클로버, 
    S   D   H   C
    A(1), 2~10, J(11), Q(12), K(13)라벨
    4개의 무늬별로 각각 13장씩 52장의 카드가 있는 모음
    
    S:카드에 대한 정보
    S는 TXY꼴로 이루어져있으며, T는 카드의 무늬, XY는 카드의 숫자
    '''
    st=input()
    lst = [[0]*13 for _ in range(4)]
    ans=[0,0,0,0]
    for i in range(0,len(st),3):
        if not lst[dct[st[i]]][int(st[i+1]+st[i+2])-1]:
            lst[dct[st[i]]][int(st[i+1]+st[i+2])-1]=1
        else:
            print(f'#{tc} ERROR')
            break
    else:
        for idxl,lt in enumerate(lst):
            for num in lt:
                if num==0:
                    ans[idxl]+=1
        else:
            print(f'#{tc}', *ans)
