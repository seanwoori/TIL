import sys
sys.stdin = open('input.txt', 'r')

T=int(input())
for tc in range(1, 1+T):
    '''
    의석이는 칠판에 글자들을 수평으로 일렬로 나열
    공백이 있을 수 있음.
    공백이 있다면 pass
    '''
    arr=[input() for _ in range(5)]
    mx_len=0
    for st in arr:
        if mx_len<len(st):
            mx_len=len(st)

    garr = [[] for _ in range(5)]
    for idx,st in enumerate(arr):
        for ch in st:
            garr[idx].append(ch)
        else:
            if len(garr[idx])<mx_len:
                while len(garr[idx])!=mx_len:
                    garr[idx].append(-1)
    sarr=list(zip(*garr))
    s=''
    for lst in sarr:
        for ch in lst:
            if ch!=-1:
                s+=ch
            else:
                continue

    print(f'#{tc} {s}')