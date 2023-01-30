import random
students = ['고영진','구본웅','김성용','김하늘','김하림',
            '김현아','민경현','배이경','서동훈','송준우',
            '심현재','유창재','윤민영','윤태영','이민호',
            '이성섭','이성우','이영아','이예슬','임수형',
            '임혜진','정선재','정현아','진익근','최태호',
            '최홍준','하정호','허주혁']
students_set = set()
def set_default() :
    global students_set
    try :
        students_set = set(open("students_set.txt", "r").read().split())
    except :
        f = open("students_set.txt", "w")
        for s in students :
            f.write(f"{s} ")
        f.close()
        students_set = set(open("students_set.txt", "r").read().split())
    print("조 배정이 가능한 사람들")
    print(*sorted(students_set), sep=" ")
    print(f"{len(students_set)} / 28")
    init = ""
    if not students_set :
        print("배정 가능한 인원이 없어서 조 배정을 초기화합니다")
        init = "ㅇㅇ"
    else :
        init = input("전체 조 배정 초기화? (ㅇㅇ : yes, 그외 : no)")
    if init == "ㅇㅇ" :
        f = open("students_set.txt", "w")
        for s in students :
            f.write(f"{s} ")
        f.close()
        students_set = set(open("students_set.txt", "r").read().split())
        print("조 배정이 가능한 사람들")
        print(*sorted(students_set), sep=" ")
        print(f"{len(students_set)} / 28")

set_default()

number = 0
while not 2 <= number <= 6:
    try :
        number = int(input("조원 수 설정 (최소 2, 최대 6): "))
    except :
        print("정수 입력")
print("조원 수 :", number)

include = ""
include = input("자신 포함? (ㅇㅇ : yes, 그외 : no) ")
person = ""
if include == "ㅇㅇ" :
    person = input("자신의 이름 입력 : ")
    while person not in students :
        print("유효한 이름이 아님(잘못된 이름이거나 이미 조 배정 완료)")
        person = input("포함할 1인 이름 : ")

group = list()
def set_group(number, person=None) :
    global group
    if person :
        print(f"{person}을(를) 포함한 {number}명만큼 조 배정")
        group = [person] + random.sample(list(students_set), min(len(students_set), number - 1))
        print("배정된 조 :", *group)
    else :
        print(f"{number}명만큼 조 배정")
        group = random.sample(list(students_set), min(len(students_set), number))
        print("배정된 조 :", *group)

confirm = None
while not confirm :
    set_group(number, person)
    temp_confirm = input("조 확정?(ㅇㅇ : yes, 그외 : no) ")
    if temp_confirm == "ㅇㅇ" :
        students_set -= set(group)
        print(f"남은 인원 : {len(students_set)} / 28")
        f = open("students_set.txt", "w")
        for s in list(students_set) :
            f.write(f"{s} ")
        f.close()
        confirm = True




    


