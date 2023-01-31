import random

names=   [
    '고영진','구본웅','김성용','김하늘','김하림',
    '김현아','민경현','배이경','서동훈','송준우',
    '심현재','유창재','윤민영','윤태영','이민호',
    '이성섭','이성우','이영아','이예슬','임수형',
    '임혜진','정선재','정현아','진익근','최태호',
    '최홍준','하정호','허주혁'
  ]


cls=[]

for i in range(1, len(names)+1):
    if len(names)>=4:
        picker = random.sample(names,4)
        cls.append(picker)
    
        for j in picker:
            if j in names:
                names.remove(j)
    else: break
print('~*~*~1반 밥 파티 뽑기~*~*~')
num=1
for i in cls:
    print(f'~~{num}조 점심 파티장: >>{i[0]}<< | 파티원: >>{i[1]}, {i[2]}, {i[3]}<<~~')
    num+=1
print('맛있는 점심 되세요 ^____^***')
# 4인 1조 => 총 7개조
# 젤 첨 뽑힌 사람이 그 조 대장. 밥먹자고 주도해야 함