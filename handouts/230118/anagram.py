words = ['eat','tea','tan','ate','nat','bat']


def group_anagrams(words):
    word_dic = {}
    for word in words:
        sub_dic = {}
        for char in word:
            if char in sub_dic:
                sub_dic[char] += 1
            else:
                sub_dic[char] = 1
        word_dic[word] = sub_dic

    anagram = []
    for word in words:
        for ana_list in anagram:
            ana_word = ana_list[0]
            if word_dic[word] == word_dic[ana_word]:
                ana_list.append(word)
                break
        else:
            anagram.append([word])
    return anagram        


print(group_anagrams(words))





words = ['eat','tea','tan','ate','nat','bat']

def group_anagrams(words):
    anagrams = {}

    for word in words:
        sorted_word = sorted(word)
        key = ''.join(sorted_word)

        if key in anagrams:
            anagrams[key].append(word)
        else:
            anagrams[key] = [word]

    return list(anagrams.values())
print(group_anagrams(words))


dic_a = {'a':1, 'b':2}
dic_b = {'b':2, 'a':1}
lst_a = [1,2]
lst_b = [2,1]
print(dic_a == dic_b)
print(dic_a is dic_b)