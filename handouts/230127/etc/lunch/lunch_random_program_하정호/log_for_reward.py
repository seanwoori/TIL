def log_in_10F():
    read_file = open("database.txt", "r", encoding='UTF8')
    seoul_01_data_10F = eval(read_file.readline())
    read_file.close()

    print("===================10층 로그 확인===================")
    print("[시스템] 교육생 '이름'을 입력하거나, '전체'를 입력하세요.")
    print("입력을 종료하려면 'N' 또는 'n'을 입력하여 주십시오.")
    while True:
        name = input("입력 : ")
        if name == 'n' or name == 'N': break
        elif name == '전체':
            for k, v in seoul_01_data_10F.items():
                print(f"{k} : {v}회")
            continue
        elif name not in seoul_01_data_10F.keys():
            while name not in seoul_01_data_10F.keys():
                print('[시스템] 서울_01반 소속 인원이 아닙니다. 이름을 올바르게 입력하여 주십시오.')
                name = input('입력 : ')
        print(f"{name} : {seoul_01_data_10F[name]}회")

def log_in_20F():
    read_file = open("database.txt", "r", encoding='UTF8')
    seoul_01_data_10F = eval(read_file.readline())
    seoul_01_data_20F = eval(read_file.readline())
    read_file.close()

    print("===================20층 로그 확인===================")
    print("[시스템] 교육생 '이름'을 입력하거나 '전체'를 입력하세요.")
    print("입력을 종료하려면 'N' 또는 'n'을 입력하여 주십시오.")
    while True:
        name = input("입력 : ")
        if name == 'n' or name == 'N': break 
        elif name == '전체':
            for k, v in seoul_01_data_20F.items():
                print(f"{k} : {v}회")
            continue
        elif name not in seoul_01_data_20F.keys():
            while name not in seoul_01_data_20F.keys():
                print('[시스템] 서울_01반 소속 인원이 아닙니다. 이름을 올바르게 입력하여 주십시오.')
                name = input('입력 : ')
        print(f"{name} : {seoul_01_data_20F[name]}회")

def log_in_total():
    read_file = open("database.txt", "r", encoding='UTF8')
    seoul_01_data_10F = eval(read_file.readline())
    seoul_01_data_20F = eval(read_file.readline())
    read_file.close()

    print("===================통합 로그 확인===================")
    print("[시스템] 교육생 '이름'을 입력하거나 '전체'를 입력하세요.")
    print("입력을 종료하려면 'N' 또는 'n'을 입력하여 주십시오.")
    while True:
        name = input("입력 : ")
        if name == 'n' or name == 'N': break
        elif name == '전체':
            for k, v in seoul_01_data_10F.items():
                print(f"{k} : {v + seoul_01_data_20F[k]}회")
            continue
        elif name not in seoul_01_data_10F.keys():
            while name not in seoul_01_data_10F.keys():
                print('[시스템] 서울_01반 소속 인원이 아닙니다. 이름을 올바르게 입력하여 주십시오.')
                name = input('입력 : ')
        print(f"{name} : {seoul_01_data_10F[name] +seoul_01_data_20F[name]}회")