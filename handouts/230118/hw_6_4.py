# A.    입력 예시 
# ['eat','tea','tan','ate','nat','bat']

# B.    출력 예시 
# [ ['eat', 'tea', 'ate'], ['tan', 'nat'], ['bat'] ] 

str_lst = ['eat','tea','tan','ate','nat','bat']

org_val_lst = []
sort_val_lst = []
idx_lst = []

for idx, value in enumerate(str_lst):
    org_val_lst.append(value)
    sort_val_lst.append(''.join(sorted(value)))
    idx_lst.append(idx)


org_dict = dict(zip(idx_lst, org_val_lst)) 
sort_dict = dict(zip(idx_lst, sort_val_lst))

new_sort_dict = sorted(sort_dict.items(), key = lambda x : x[1])
org_sort_set = []

for i in range(len(new_sort_dict)):
    org_sort_set.append(new_sort_dict[i][1])
new_sort_set = list(set(org_sort_set))


answer = []

for char_1 in new_sort_set:    
    temp_answer = []
    for i in range(len(sort_dict)):
        if char_1 == sort_dict[i]:
            temp_answer.append(org_dict[i])
        else:
            pass

    answer.append(temp_answer)

print(answer)

# 교수님 풀이 1
'''
key값으로 sorted된 값,
value값으로 origin 값을 넣음.

이후 if문을 통해 참값은 새로운 리스트에 넣어주고
틀린값은 string으로 넣어줌
이후 list()를 통해 value값만 리스트로 반환
'''

# 교수님 풀이 2
'''
각 단어에서 알파벳 갯수만 뽑아온 dictionary를 만듦.
이후 리스트를 돌며 알파벳 갯수가 동일한 것들의 집합을 만듦.
딕셔너리는 순서가 없음. 따라서 리스트와 달리 순서가 다르지만 key, value값이 같으면 두 딕셔너리는 같음.
'''
