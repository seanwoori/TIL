import sys
sys.stdin = open('input.txt', 'r')

T = int(input())
for tc in range(1, 1+T):
    st1 = list(set(input())) # st1을 고유 원소 리스트로 반환
    st2 = list(map(str, input()))

    cnt_lt = []
    for char1 in st1:
        cnt = 0
        for char2 in st2:
            if char1 == char2:
                cnt += 1
        cnt_lt.append(cnt)

    print(f'#{tc} {max(cnt_lt)}')