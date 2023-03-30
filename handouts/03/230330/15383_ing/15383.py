import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1,1+T):
    N,E = map(str, input().split()) # N은 숫자, E는 교환 횟수
    lst=[]
    for st in N:
        lst.append(int(st))

    
    print(f'#{tc} {ans}')