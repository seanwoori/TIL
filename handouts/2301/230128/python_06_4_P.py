entry_record = ['이싸피', '박장고', '조실습', '이싸피', '조실습', '오디비', '임온실', '조실습', '조실습', '이싸피', '안도둑', '임온실', '최이썬', '오디비', '안도둑', '염자바', '박장고', '조실습',
                '최이썬', '조실습', '염자바', '박장고', '임온실', '임온실', '이싸피', '임온실', '오디비', '조실습', '염자바', '임온실', '박장고', '최이썬', '안도둑', '염자바', '임온실', '박장고', '이싸피', '안도둑',
                '임온실', '오디비', '최이썬', '안도둑', '이싸피', '오디비', '안도둑', '이싸피', '박장고', '박장고', '안도둑', '안도둑', '안도둑', '염자바', '최이썬', '오디비', '오디비', '최이썬', '이싸피', '임온실', '안도둑']

exit_record = ['최이썬', '조실습', '이싸피', '안도둑', '임온실', '안도둑', '이싸피', '오디비', '염자바', '박장고', '최이썬', '이싸피', '염자바', '염자바', '박장고', '임온실', '이싸피',
               '박장고', '안도둑', '염자바', '이싸피', '조실습', '조실습', '임온실', '박장고', '이싸피', '조실습', '박장고', '오디비', '안도둑', '조실습', '임온실', '안도둑', '안도둑', '임온실', '조실습', '최이썬', '안도둑', '임온실',
               '염자바', '이싸피', '임온실', '안도둑', '오디비', '안도둑', '오디비', '임온실', '염자바', '임온실', '박장고', '조실습', '이싸피', '최이썬', '최이썬', '오디비', '오디비', '염자바', '오디비', '안도둑', '박장고']

from collections import Counter

dict_ent = dict(Counter(entry_record))
dict_ext = dict(Counter(exit_record))
sort_ent = dict(sorted(dict_ent.items(), key = lambda x:x[1], reverse=True))

sort_key_ent = dict(sorted(dict_ent.items(), key = lambda x:x[0], reverse=True))
sort_key_ext = dict(sorted(dict_ext.items(), key = lambda x:x[0], reverse=True))

print('입장 기록 많은 Top3')
i = 0
for key, val in sort_ent.items():
    print(f'{key} {val}회')
    i += 1
    if i >= 3:
        break

for key, val in sort_key_ent.items():
    if val > sort_key_ext[key]:
        print(f'{key}는 입장 기록이 {val-sort_key_ext[key]}회 더 많아 수상합니다.')
    elif val < sort_key_ext[key]:
        print(f'{key}는 퇴장 기록이 {sort_key_ext[key]-val}회 더 많아 수상합니다.')
    else:
        pass