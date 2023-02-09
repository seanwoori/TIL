import sys
sys.stdin = open('input.txt', 'r', encoding='utf-8')

T = int(input())
for tc in range(1, 1+T):
    a = input()
    b = input()
    ans = 0

    for i in range(len(b)-len(a)+1):
        if a in b[i:i+len(a)]:
            ans += 1


    print(f'#{tc} {ans}')
