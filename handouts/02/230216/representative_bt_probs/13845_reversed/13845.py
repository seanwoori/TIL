import sys
sys.stdin = open('input.txt', 'r')

'''
토너먼트로 한 명을 뽑는 게임
전체를 두 그룹으로 나누고 그룹의 승자끼리 카드를 비교해서 이긴 사람 고르기
번호가 같은 경우, 앞에 있는 쪽이 승자.
1:가위
2:바위
3:보
처음 노드부터 내려가기에는 너무 경우의 수가 많아짐.
거꾸로 올라가는 방법은?
자료 탐색에서 거꾸로 올라갈 수는 없을까?
아니면 정방향으로 내려가는데, 단위 행위를 거꾸로 해석할 수 있는 방법은?
1
1 3 4
3 1 4
1 1 2

2
2 1 3
1 2 3
2 2 4

3
2 3 5
3 2 5
3 3 6
'''

def solve(s,e):
    if s==e:
        return s
    else:
        # 왼쪽 승자
        a = solve(s, (s+e)//2)
        # 오른쪽 승자
        b = solve((s+e)//2+1, e)
        if (lst[a]%3)+1 == (lst[b]):
            return b
        return a

T = int(input())
for tc in range(1, 1+T):
    N = int(input())
    lst = [0]+list(map(int, input().split()))

    ans = solve(1, N)
    print(f'#{tc} {ans}')