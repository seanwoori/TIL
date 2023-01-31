import random

def make_company(people_dict, n):
    temp_lst = [key for key in people_dict if people_dict[key] == '참여']
    result_lst = []

    while len(temp_lst) > 0:
        if len(temp_lst) >= n:
            samples = random.sample(temp_lst, n)
            result_lst.append(samples)
            
            for person in samples:
                temp_lst.remove(person)

        else:
            for index in range(len(temp_lst)):
                result_lst[index].append(temp_lst[index])
            else:
                temp_lst = []

    return result_lst
    

