lst_a = []

for i in range(1,1000):
    if i % 2 == 0 or i % 7 == 0:
        lst_a.append(i)

print(sum(lst_a))

