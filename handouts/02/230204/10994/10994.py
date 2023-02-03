#n = int(input())
n = 5

'''
1   1                               1
2   5 2 2+1 2 5                     5
3   9 2 5+2 2+2 3+2 2+2 5+2 2 9     9
'''
n_his = []
for i in range(n):
    n_his.append(1 + (2**2) * i)
ans = []

# n_cri : 1 5 9 13 ...
# i : 0 01234 012345678 ...
# temp : [[*****], [*       *] ...]
# ans : [temp(1), temp(5), temp(9)...]
for n_cri in n_his:
    temp = []
    for i in range(n_cri):
        if (i == 0) or (i == n_cri - 1):
            temp.insert(i, ['*'] * n_cri)
        elif (i == 1) or (i == n_cri - 2):
            temp.insert(i, ['*'] + [' '] * (n_cri-2) + ['*'])
        else:
            temp.insert(i, ['*'] + [' '] +ans[n_his.index(n_cri)-1][i-2] + [' '] + ['*'])

    ans.append(temp)

for i in range(n_cri):
    a = ans[n_his.index(n_cri)][i]
    print(''.join(a))