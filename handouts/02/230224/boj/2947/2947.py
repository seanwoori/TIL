import sys
sys.stdin = open('input.txt', 'r')

def bubble_sort(lst):
    while True:
        flag=False
        for i in range(len(lst)-1):
            if lst[i]>lst[i+1]:
                lst[i],lst[i+1]=lst[i+1],lst[i]
                print(*lst)
                flag=True
        else:
            if not flag:
                break

lst=list(map(int, input().split()))
bubble_sort(lst)