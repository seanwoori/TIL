# 10진법으로 표현된 대상 수 n을 목표 진법 q로 변환하는 함수 change(n,q)
def change(n,q):
    '''
    :param n: 10진법으로 표현된 대상 수 n
    :param q: q진법 변환을 위한 변수 q
    :return:  q진법으로 변환된 결과값을 str으로 return
    '''

    # 나머지를 저장할 st 변수 선언
    st=''

    # 몫이 0이될 때 까지 while loop 진행
    while n>0:

        # 내장함수 divmod를 이용하여 몫과 나머지를 도출
        # 이후 몫을 n변수에 갱신
        # st 변수에 나머지 저장
        n,mod=divmod(n,q)
        st+=str(mod)

    # 결과값은 st 저장값의 역순이므로,
    return st[::-1]

T=int(input())
for tc in range(1,1+T):
    _ = int(input())
    num=input()

    # st_bin은 16진수 num을 10진법으로 바꾼 후, 2진수로 바꾼 str 자료형이 저장됨
    st_bin = change(int(num,16),2)

    # 연속된 '1'을 카운트하기 위한 cnt, 최대값 저장을 위한 ans
    cnt=0
    ans=0


    for s in st_bin:
        if s=='1':
            cnt+=1
        else:
            # 만약 s=='0'이고 cnt가 ans보다 크다면,
            # ans 갱신
            # cnt 초기화
            if ans<=cnt:
                ans=cnt
            cnt=0

    # 이진수가 1로 끝나면서 최대값일 경우를 고려하기 위한 for else문
    else:
        if ans<=cnt:
            ans=cnt

    print(f'#{tc} {ans}')