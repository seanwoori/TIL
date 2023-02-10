import sys
sys.stdin = open('input.txt', 'r')

def dia(lst):
    lst = []
    if len(lst):
        for i in range(5):
            temp = []
            for j in range(5):
                if i==0 or i==4:
                    temp.append('..#..')
                elif i==1 or i==2:
                    temp.append('.#.#.')
                else:
                    temp.append()



T = int(input())
for tc in range(1, 1+T):
    lst = list(map(str, input()))
    print(lst)