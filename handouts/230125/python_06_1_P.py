# A. 입력예시
#print(de_identify('970103-1234567'))
#print(de_identify('8611232345678'))

# B. 출력예시
# 970103*******
# 861123******* 

def de_identify(word):

    str_word = ''
    
    for char in word:
        if char == '-':
            char = ''
            str_word += char
        else:
            str_word += char
    
    i = 0
    
    de_iden = ''

    for char in word:
        i += 1
        print(char)
        if i >= 7:
            char = '*'
            de_iden += char
        else:
            de_iden += char

    return de_iden



print(de_identify('970103-1234567'))
print(de_identify('8611232345678'))