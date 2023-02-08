import sys
sys.stdin = open('input.txt', 'r')

# 시퀀셜하게 모든 것을 조건판별하면 코드 실행 속도가 매우 늦어짐
# 하지만 파이썬은 딕셔너리라는 매우 좋은 기능이 있음. 이는 다른 언어에서는 제공하지 않음.
# 딕셔너리를 바탕으로 코드를 작성하면 룩업 테이블을 참조하듯 검색할 수 있음.

# tbl = [0] * 128
# tbl[ord('b')] = 'd'
# tbl[ord('d')] = 'b'
# tbl[ord('p')] = 'q'
# tbl[ord('q')] = 'p'
dct = {'b':'d', 'd':'b', 'p':'q', 'q':'p'}

T = int(input())
for tc in range(1, 1+T):
    a = str(input())[::-1]
    alst = []
    for ch in a:
        # alst.append(tbl[ord(ch)])
        alst.append(dct[ch])
    print(f'{tc} {''.join(map(str,alst))}')
