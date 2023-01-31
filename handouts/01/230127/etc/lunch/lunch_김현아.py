import random



lst = [
    '고영진','구본웅','김성용','김하늘','김하림',
    '김현아','민경현','배이경','서동훈','송준우',
    '심현재','유창재','윤민영','윤태영','이민호',
    '이성섭','이성우','이영아','이예슬','임수형',
    '임혜진','정선재','정현아','진익근','최태호',
    '최홍준','하정호','허주혁'
  ]

"""
셔플하고 4개씩 쪼갠다?
lst[i:i+4] 하고 i... 4씩 증가?
"""

random.shuffle(lst)
# print(lst)

# def lunch(a, b):
#     for i in range(0, len(a), b):
#         return [a[i:i+b]]

# print(lunch(lst, 4))

# ...? 왜 하나만 나오지...
# 빈리스트에 추가?

def lunch(a, b):
    new = []
    for i in range(0, len(a), b):
        new.append(a[i:i+b])
    return new

print(lunch(lst, 4))

