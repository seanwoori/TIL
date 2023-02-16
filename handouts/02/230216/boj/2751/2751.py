import sys
sys.stdin = open('input.txt', 'r')
# 퀵소트 함수를 작성하여 문제 풀이
'''
def qsort(lst):
    if len(lst) < 2:
        return lst
    else:
        p = lst.pop(len(lst)//2)
        l = []
        r = []
        for num in lst:
            if num < p :
                l.append(num)
            else:
                r.append(num)
        return qsort(l)+[p]+qsort(r)
'''
T = int(input())
lst = []
for _ in range(T):
    lst.append(int(input()))
lst.sort()
for num in lst:
    print(num)