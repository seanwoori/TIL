import sys
sys.stdin = open('input.txt', 'r')

T = 10
for tc in range(1, 1+T):
    _, st = map(str, input().split())
    org = list(st)
    flag = True
    # org list를 처음부터 끝까지 순회
    while flag:
        for i in range(len(org)-1):
            # 만약 연속되는 문자가 같다면,
            # str는 lst에 저장
            if org[i]==org[i+1]:
                l=org[:i]
                r=org[i+2:]
                # l과 r을 따로 저장한 다음에, 이후 문자열 끝까지 순회.
                while len(l)>0 and len(r)>0:
                    if l[-1]==r[0]:
                        l.pop()
                        r.pop(0)
                    else:
                        break
                org = l+r
                break
        else:
            flag = False
        # lst에 저장된 str들에 대하여, 가장 길이가 긴 것이 ans

    ans=''.join(org)
    print(f'#{tc} {ans}')
