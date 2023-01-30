'''
고려사항(우선)
- 사용자 입력 받기 (한 명 씩 입력)
- 10층, 20층 구분
- 층 별로 인원수가 딱 떨어지는 숫자로 조 편성(3,4,5 중 하나)
- 딱 떨어지지 않을 경우 4명 조를 기본으로하고 나머지 편성 => 특정 경우 나머지가 1명이 되는데, 1명은 팀 선택 특권(사실 이렇게 안하면 하드코딩이 될 듯하여 패스 - 모든 소수 경우의 수)
- 프로그램 사용자 기록 남기기 => reward 시스템 적용 => txt 파일로 뿜자(Database로 사용)

고려사항(확장용)
- 일정 카테고리로 정렬된 dict로 value값을 삼으면 좀 더 성향에 맞는 사람끼리 주선도 할 수 있을 것 같다. => 하지만 랜덤 프로그램이라는 목적이 희미해질듯.
- 함수 분할 필요.

수정 필요
- 오입력에 대한 처리 필요
- DB를 .txt로 사용함 => DB연결이 베스트, 혹은 txt 파일 보안 필요
- 주석을 너무 메모하듯 사용. 주석 정리 필요
- 특정 소수(prime num)에서 4명 그룹으로 처리하면 애매해지는 경우 발생. 예외 케이스에 대한 대처를 추가할 필요가 있음.
- 현재 .txt(DB)를 불러오는 방식과 eval() 함수를 사용하는 것이 레거시하다는 느낌이 든다. 공부하여 수정이 필요(.txt => 프레임워크를 통함 DB 연결, eval() => json 모듈 활용)
- reward에 대한 서비스 기획 필요(+ 초기화 시점)
- 분할 및 하드코드에 대한 리팩토링 필요
'''
import random # random 모듈 사용 : 임의 수 사용을 위함
import log_for_reward

# import json # dict to str, str to dict => 현재는 eval로 사용

def lunch_random_program():
    
    read_file = open("database.txt", "r", encoding='UTF8') # 오픈될 텍스트 파일(DB)을 상대 경로로 지정
    seoul_01_data_10F = eval(read_file.readline()) # eval(expression) : expression은 문자열 형식의 `식`을 의미함. 즉, 식이 문자열로 제공되었을때 문자열 그대로 파이썬 실행을 할 수 있게 돕는 함수이다.
    seoul_01_data_20F = eval(read_file.readline())
    read_file.close()
    
    write_file = open("database.txt", "w", encoding='UTF8')

    seoul_01_name_list_10F = []
    seoul_01_name_list_10F_random = []
    seoul_01_name_list_20F = []
    seoul_01_name_list_20F_random = []
    
    print("=======================10층 희망자=======================")
    print("[시스템] 이름을 입력하여 주십시오. 입력을 종료하려면 'N' 또는 'n'을 입력하여 주십시오.")
    for i in range(28): # 28명 기본으로 전체 순회
        input_user = input('입력 : ')
        if input_user == 'N' or input_user == 'n':
            break
        # elif input_user not in seoul_01_data_10F.keys():  # 왜 이 코드가 없고 while 만 있으면 안잡히지? 
        while input_user not in seoul_01_data_10F.keys():
            print('[시스템] 서울_01반 소속 인원이 아닙니다. 이름을 올바르게 입력하여 주십시오.')
            input_user = input('입력 : ')
                # if input_user == 'N' or input_user == 'n':
                #     break
        seoul_01_name_list_10F.append(input_user)
        seoul_01_data_10F[input_user] += 1

    num_of_people = len(seoul_01_name_list_10F)
    random.shuffle(seoul_01_name_list_10F)
    if num_of_people % 3 == 0:
        seoul_01_name_list_10F_random = [seoul_01_name_list_10F[i:i+3] for i in range(0, len(seoul_01_name_list_10F), 3)]
    elif num_of_people % 4 == 0:
        seoul_01_name_list_10F_random = [seoul_01_name_list_10F[i:i+4] for i in range(0, len(seoul_01_name_list_10F), 4)]
    elif num_of_people % 5 == 0:
        seoul_01_name_list_10F_random = [seoul_01_name_list_10F[i:i+5] for i in range(0, len(seoul_01_name_list_10F), 5)]
    else:
        seoul_01_name_list_10F_random = [seoul_01_name_list_10F[i:i+4] for i in range(0, len(seoul_01_name_list_10F), 4)]
    print(seoul_01_name_list_10F_random)


    print("=======================20층 희망자=======================")
    print("[시스템] 이름을 입력하여 주십시오. 입력을 종료하려면 'N' 또는 'n'을 입력하여 주십시오.")
    for i in range(28): # 28명 기본으로 전체 순회
        input_user = input('입력 : ')
        if input_user == 'N' or input_user == 'n':
            break
        elif input_user not in seoul_01_data_20F.keys():
            while input_user not in seoul_01_data_20F.keys():
                print('[시스템] 서울_01반 소속 인원이 아닙니다. 이름을 올바르게 입력하여 주십시오.')
                input_user = input('입력 : ')
                # if input_user == 'N' or input_user == 'n':
                #     break
        seoul_01_name_list_20F.append(input_user)
        seoul_01_data_20F[input_user] += 1

    num_of_people = len(seoul_01_name_list_20F)
    random.shuffle(seoul_01_name_list_20F)
    if num_of_people % 3 == 0:
        seoul_01_name_list_20F_random = [seoul_01_name_list_20F[i:i+3] for i in range(0, len(seoul_01_name_list_20F), 3)]
    elif num_of_people % 4 == 0:
        seoul_01_name_list_20F_random = [seoul_01_name_list_20F[i:i+4] for i in range(0, len(seoul_01_name_list_20F), 4)]
    elif num_of_people % 5 == 0:
        seoul_01_name_list_20F_random = [seoul_01_name_list_20F[i:i+5] for i in range(0, len(seoul_01_name_list_20F), 5)]
    else:
        seoul_01_name_list_20F_random = [seoul_01_name_list_20F[i:i+4] for i in range(0, len(seoul_01_name_list_20F), 4)]
    print(seoul_01_name_list_20F_random)

    str_data_to_DB = str(seoul_01_data_10F) + '\n' + str(seoul_01_data_20F)
    write_file.write(str_data_to_DB)
    write_file.close()

print("[시스템] 사용하고자 하는 기능을 선택하여 주십시오. (숫자 1 혹은 2 입력)")
print("1: 점심 랜덤 매칭 프로그램, 2: 10층 사용 기록 조회, 3: 20층 사용 기록 조회, 4: 통합 사용 기록 조회")
user_input = int(input())
if user_input == 1:
    lunch_random_program()
elif user_input == 2:
    log_for_reward.log_in_10F()
elif user_input == 3:
    log_for_reward.log_in_20F()
elif user_input == 4:
    log_for_reward.log_in_total()

