import json


def dec_movies(movies):
    movie = open('./data/movies.json', encoding='utf-8')

    movie_detail = json.load(movie)

    id_vals = []

    for mov_dic in movie_detail:
        id_vals.append(mov_dic.get('id'))
    

    dec_lst = []
    
    for keys in id_vals:
        url_files = open(f'./data/movies/{keys}.json', encoding='utf-8')
        details = json.load(url_files)
        if details.get('release_date').split('-')[1] == '12': 
            print(details.get('release_date').split('-'))
            dec_lst.append(details.get('title'))
    
    return dec_lst

    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)
    
    print(dec_movies(movies_list))
