from ..data.launch_people import *
from ..control import *
from ..exception.is_wrong_person import *

def get_non_participation(class_1_members):
    while True:
        notice_str = "\n미참여자를 다음과 같은 형식으로 입력하세요\
            \nex : 짱구 철수 유리 훈이 ...\
            \n없을 경우 입력을 안해도 괜찮습니다!\n\n"
        non_participation_lst = list(input(notice_str).split())

        if is_wrong_person(non_participation_lst, class_1_members.launch_info):
            print("\n**********************************************************\
                \n1반이 아닌 인원이 포함되어 있습니다. 다시 입력해주세요.\
                \n**********************************************************")
            continue
        
        make_non_participation.make_non_participation(non_participation_lst, class_1_members)
        break

    temp_lst = [person for person in class_1_members.launch_info if class_1_members.launch_info[person] == '미참여']

    if len(temp_lst) == 0:
        print("미참여자는 없습니다!!")
    else:
        print("\n미참여자는 다음과 같습니다.")
        print(temp_lst)
    
    return temp_lst

