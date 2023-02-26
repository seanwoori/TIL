import sys
sys.stdin = open('input.txt', 'r')

def mx(l):
    for i in range(len(l)-1):
        # max 일때, lst[i]가 max(lst[i+1:j]) 보다 작으면 for loop 시작
        if l[i]<max(l[i+1:]) and max(l[i+1:])!=0:
            # 가장 낮은 자리수에 있는 것과 교환
            for j in range(i+1, len(l))[::-1]:
                if l[j]==max(l[i+1:]):
                    l[i],l[j]=l[j],l[i]
                    return l
    return l

def mn(l):


    for i in range(len(l)-1):
        # ,in 일때, lst[i]가 min(lst[i+1:j]) 보다 작으면 for loop 시작
        # min값이 0이면, temp에 lst를 복사하여 0을 지우면서 다음 min값을 찾음.
        if min(l[i+1:]) == 0:
            temp = list(set(l[i+1:]))
            temp.remove(0)
            if temp == l[i+1:]:
                return l
            else:
                mnval = min(temp)
        else:
            mnval=min(l[i+1:])

        if l[i]>mnval and mnval!=0:
            # 가장 낮은 자리수에 있는 것과 교환
            for j in range(i+1, len(l)):
                if l[j]==mnval:
                    l[i],l[j]=l[j],l[i]
                    return l
    return l

T=int(input())
for tc in range(1, 1+T):
    lst=list(map(int,input()))
    tmnlst=lst[:]
    tmxlst=lst[:]
    mxlst=mx(tmxlst)
    mnlst=mn(tmnlst)
    mmnn = ''
    mmxx = ''

    # N이 한자리수일때
    if len(lst)==1:
        mmxx=mmnn=str(lst[0])
    # N이 두자리수 이상일때
    else:
        for i in range(len(lst)):
            mmxx+=str(mxlst[i])
            mmnn+=str(mnlst[i])

    print(f'#{tc} {mmnn} {mmxx}')
