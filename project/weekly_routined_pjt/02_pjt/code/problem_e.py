import requests
from pprint import pprint
import config

def credits(title):
    key = config.TMDB_API_KEY
    url_src_mov = 'https://api.themoviedb.org/3/search/movie?api_key=' + str(key) + '&language=ko-KR&query=' + title   
    resp_src = requests.get(url_src_mov).json()            
    
    if resp_src['total_pages'] == 0:
        return None
    
    rslt_src = resp_src['results']        
    
    lst_ids = []
    
    for dict in rslt_src:
        lst_ids.append(dict['id'])

    result = {}
    act_lst = []
    dir_lst = []
    
    for ids in lst_ids:
        url_rec_mov = 'https://api.themoviedb.org/3/movie/' + str(ids) + '/credits?api_key=' + str(key) + '&language=ko-KR'
        resp_rec = requests.get(url_rec_mov).json()  

        if 'status_code' in resp_rec.keys():
            return None

        cast_dict = resp_rec['cast']
        crew_dict = resp_rec['crew']


        for dict in cast_dict:
            if dict['known_for_department'] == 'Acting':    
                if dict['cast_id'] < 10:
                    act_lst.append(dict['name'])
            elif dict['known_for_department'] == 'Directing':
                dir_lst.append(dict['name'])
        
        for dict in crew_dict:
            if dict['known_for_department'] == 'Directing':
                dir_lst.append(dict['name'])

    
    result['cast'], result['crew'] = act_lst, list(set(dir_lst))
    
    return result    

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화 id를 통해 영화 상세정보를 검색하여 주연배우 목록(cast)과 스태프(crew) 중 연출진 목록을 반환
    영화 id 검색에 실패할 경우 None을 반환
    """
    pprint(credits('기생충'))
    # {'cast': ['Song Kang-ho', 'Lee Sun-kyun', ..., 'Jang Hye-jin'], 'crew': ['Bong Joon-ho', 'Park Hyun-cheol', ..., 'Yoon Young-woo']}
    pprint(credits('검색할 수 없는 영화'))
    # None
