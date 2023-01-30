import random as rd


def random_lunch(code, *n):
    lst = [
    '고영진', '구본웅', '김성용', '김하늘', '김하림',
    '김현아', '민경현', '배이경', '서동훈', '송준우',
    '심현재', '유창재', '윤민영', '윤태영', '이민호',
    '이성섭', '이성우', '이영아', '이예슬', '임수형',
    '임혜진', '정선재', '정현아', '진익근', '최태호',
    '최홍준', '하정호', '허주혁']
    lst_ma = ['고영진', '구본웅', '김성용', '민경현', '서동훈', '송준우',
              '심현재', '유창재', '윤태영', '이민호', '이성섭', '이성우', 
              '임수형', '정선재', '진익근', '최태호', '최홍준', '하정호',
              '허주혁']
    lst_fe = ['김하늘', '김하림', '김현아', '배이경', '윤민영', '이영아',
              '이예슬', '임혜진', '정현아']
    
    cnt = 0
    total = len(lst)
    
    if code == 'random':
        rd.shuffle(lst)
        team = list()
        dummy = list()
        
        for i in lst:
            cnt += 1
            dummy.append(i)

            if cnt == n[0]:
                team.append(dummy)
                cnt = 0
                dummy = list()

        if len(dummy) != 0:
            team.append(dummy)
            
    elif code == 'seperate':
        rd.shuffle(lst_fe)
        rd.shuffle(lst_ma)
        team = list()
        dummy = list()
        for i in lst_fe:
            cnt += 1
            dummy.append(i)

            if cnt == n[0]:
                team.append(dummy)
                cnt = 0
                dummy = list()

        if len(dummy) != 0:
            team[-1] = team[-1] + dummy
        
        dummy = list()
        cnt = 0
        for i in lst_ma:
            cnt += 1
            dummy.append(i)
            
            if cnt == n[1]:
                team.append(dummy)
                cnt = 0
                dummy = list()
        
        if len(dummy) != 0:
            team.append(dummy)
    
    elif code == 'balance':
        rd.shuffle(lst_ma)
        rd.shuffle(lst_fe)
        last_num = total//n[0]
        team = [[]]*(last_num)
        
        for i in lst_ma:
            if team[cnt] == []:
                team[cnt] = [i]
                
            else:
                team[cnt].append(i)
                
            cnt += 1
            if cnt == last_num:
                cnt = 0
        
        cnt = 0
        for i in lst_fe:
            team[cnt-1].append(i)
            cnt -= 1
            if cnt == -len(team):
                cnt = 0
        
    return team


if __name__ == '__main__':
    ip = int(input())
    n = int(input())
    team = random_lunch(ip, n)
