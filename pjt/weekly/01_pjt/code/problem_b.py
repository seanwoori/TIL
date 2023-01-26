import json
from pprint import pprint


def movie_info(movie, genres):
    movie = open('./data/movie.json', encoding='utf-8')
    genre = open('./data/genres.json', encoding='utf-8')
    
    movie_detail = json.load(movie)
    genre_detail = json.load(genre)

    add_dict = {}
    genre_name = []

    for value in movie_detail['genre_ids']:
        for dic in genre_detail:
            if value == dic.get('id'):
                genre_name.append(dic.get('name'))
                add_dict['genre_name'] = genre_name


    new_dict = {
        'id' : movie_detail.get('id'),
        'title' : movie_detail.get('title'),
        'poster_path' : movie_detail.get('poster_path'),
        'vote_average' : movie_detail.get('vote_average'),
        'overview' : movie_detail.get('overview'),
                }
    
    new_dict.update(add_dict)

    return new_dict 
    # 여기에 코드를 작성합니다.  
        

# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie = json.load(movie_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movie, genres_list))
