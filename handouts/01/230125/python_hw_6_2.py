# 입력 예시
# # mass percent.py 실행 시
# 1.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 1% 400g
# 2.소금물의 농도(%)와 소금물의 양(g)을 입력하십시오: 8% 300g
# Done

# 출력 예시
# 4.0% 700.0g

perc_lst = []
mss_lst = []
count = 0

while True:
    
    perc_mss = input('소금울의 농도(%)와 양(g)을 입력하시오.: ')
    if (perc_mss == 'Done'):
        break    

    count += 1
    temp_lst = []

    temp_lst = perc_mss.split()
    perc_lst.append(int(temp_lst[0].rstrip('%')))
    mss_lst.append(int(temp_lst[1].rstrip('g')))

    if count >= 5:
        break

total_salt = 0
total_water = sum(mss_lst)

for i in range(len(perc_lst)):
    total_salt += (perc_lst[i] * mss_lst[i]) / 100

perc_salt = total_salt / total_water * 100

print(f'{perc_salt}% {total_water}g')