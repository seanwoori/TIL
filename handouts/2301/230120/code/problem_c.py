import json
from pprint import pprint


def movie_info(movies, genres):
    movie = open('./data/movies.json', encoding='utf-8')
    genre = open('./data/genres.json', encoding='utf-8')
    
    movie_detail = json.load(movie)
    genre_detail = json.load(genre)



    movie_info = []   
     


        

    for mov_dic in movie_detail:    
        add_dict = {}        
        genre_name = []        
        
        lst_val = mov_dic.get('genre_ids')
        for val in lst_val:
            for gen_dic in genre_detail:            
                if val == gen_dic.get('id'):
                    genre_name.append(gen_dic.get('name'))
        
        add_dict['genre_name'] = genre_name        
        
        new_dict = {
            'id' : mov_dic.get('id'),
            'title' : mov_dic.get('title'),
            'poster_path' : mov_dic.get('poster_path'),
            'vote_average' : mov_dic.get('vote_average'),
            'overview' : mov_dic.get('overview'),
                    }

      

        new_dict.update(add_dict) 
        movie_info.append(new_dict)
    
    return movie_info
    # 여기에 코드를 작성합니다.  
        
   
# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    movies_json = open('data/movies.json', encoding='utf-8')
    movies_list = json.load(movies_json)

    genres_json = open('data/genres.json', encoding='utf-8')
    genres_list = json.load(genres_json)

    pprint(movie_info(movies_list, genres_list))
