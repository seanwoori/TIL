import random

people = [
    '고영진','구본웅','김성용','김하늘','김하림',
    '김현아','민경현','배이경','서동훈','송준우',
    '심현재','유창재','윤민영','윤태영','이민호',
    '이성섭','이성우','이영아','이예슬','임수형',
    '임혜진','정선재','정현아','진익근','최태호',
    '최홍준','하정호','허주혁'
  ]

def random_lunch():
    while True:    
        ran = random.sample(people, 4)
        print(ran)
        for i in ran:
            for idx in people:
                if i == idx:
                    people.remove(idx)
        if people == []:
            break

random_lunch()


       
    

    

