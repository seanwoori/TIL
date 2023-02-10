import sys
sys.stdin = open('input.txt', 'r')
lst = []
for _ in range(9):
    lst.append(int(input()))
temp = []
flag = False
for i in range(9):
    for j in range(i+1, 9):
        if sum(lst)-(lst[i]+lst[j]) == 100:
            temp.append(lst[i])
            temp.append(lst[j])
            flag = True
        if flag == True:
            break
    if flag == True:
        break
for n in temp:
    lst.remove(n)
lst = sorted(lst)

for num in lst:
    print(num)
