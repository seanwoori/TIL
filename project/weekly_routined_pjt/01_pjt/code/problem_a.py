import json
from pprint import pprint


def movie_info(movie):
    movie = open('./data/movie.json', encoding='utf-8')
    movie_detail = json.load(movie)
    new_dict = {
        'id' : movie_detail.get('id'),
        'title' : movie_detail.get('title'),
        'poster_path' : movie_detail.get('poster_path'),
        'vote_average' : movie_detail.get('vote_average'),
        'overview' : movie_detail.get('overview'),
        'genre_ids' : movie_detail.get('genre_ids')
                }   
    return new_dict
    

    # 여기에 코드를 작성합니다.    


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movie_json = open('data/movie.json', encoding='utf-8')
    movie_dict = json.load(movie_json)
    
    pprint(movie_info(movie_dict))
