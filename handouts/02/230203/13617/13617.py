import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):
    n, q = map(int, input().split())
    lst = []
    for i in range(q):
        lst.append(list(map(int, input().split())))
    box = [0] * n
    i = 0
    for a in lst:
        i += 1
        box[a[0]-1 : a[1]] = list(i for _ in range(a[1]-a[0]+1)) # .index()메소드 사용할 때 동일 원소에 대하여 인덱스 값은 고정. 이를 간과하여 많은 시간을 들여 디버깅함.


    print(f'#{test_case}', *box)