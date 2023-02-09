# 공통적으로 사용되는 loopup table, 라스트 등은 루프 바깥에서..(한번만)
# [1] dct 생성
tbl = ["ZRO", "ONE", "TWO", "THR", "FOR", "FIV", "SIX", "SVN", "EGT", "NIN"]
dct = {tbl[n]:n for n in range(len(tbl))}
T = int(input())
for test_case in range(1, T + 1):
    _ = input()             # 사용하지 않는 경우 명시적으로 _ 저장/표시
    lst = input().split()   # list로 문자열 저장
 
    # [2] cnts[] 누적표시
    cnts = [0]*(len(tbl))
    for st in lst:
        cnts[dct[st]]+=1
 
    # [3] 정답 문자열 완성
    ast = ""
    for i in range(len(tbl)):
        ast += (tbl[i]+" ")*cnts[i]
 
    print(f'#{test_case}',ast,sep='\n')
