import sys
sys.stdin = open("input.txt", "r")

T = int(input())
for test_case in range(1, T + 1):

    num = int(input())
    ans = []
    b = [2, 3, 5, 7, 11]

    for n in b:
        cnt = 0
        while True:
            if str(num / n).split('.')[1] == '0':
                cnt += 1
                num = num / n
            else:
                ans.append(cnt)
                break

    print(f'#{test_case}', *ans)

