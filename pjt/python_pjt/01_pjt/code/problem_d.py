import json


def max_revenue(movies):
    movie = open('./data/movies.json', encoding='utf-8')

    movie_detail = json.load(movie)

    id_vals = []

    for mov_dic in movie_detail:
        id_vals.append(mov_dic.get('id'))
    
    rev_lst = []
    title_lst = []

    for keys in id_vals:
        url_files = open(f'./data/movies/{keys}.json', encoding='utf-8')
        details = json.load(url_files)
        rev_lst.append(details.get('revenue'))
        title_lst.append(details.get('title'))

    dict_rev = dict(zip(title_lst, rev_lst))
    srt_dict_rev = sorted(dict_rev.items(), key = lambda x : x[1], reverse = True)

    return srt_dict_rev[0][0]

    # 여기에 코드를 작성합니다.  
        
        
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(max_revenue(movies_list))
