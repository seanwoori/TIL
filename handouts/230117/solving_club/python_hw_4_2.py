words = ["round" , "dream", "magnet" , "tweet" , "tweet", "trick", "kiwi"]
flag = False


for idx, char in enumerate(words):
    idx += 1
    if idx == len(words):
        break
    if words[idx][0] == words[idx-1][-1]:
        flag = True
    elif words[idx] in words[:idx]:
        print(f'fail, {idx}번째 사람의 단어 {words[idx]}가 틀렸습니다.')
    else:
        print(f'fail, {idx}번째 사람의 단어 {words[idx]}가 틀렸습니다.')
        break
if flag == True:
    print('pass')