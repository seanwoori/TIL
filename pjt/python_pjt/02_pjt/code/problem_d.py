import requests
from pprint import pprint
import config

def recommendation(title):
    '''
    url_lst = []
    for i in range(3):
        query = str(input('검색할 영화를 입력해주세요. 입력을 완료했을 경우 n 입력 : '))
        url_lst.append(url_base + query)

        if query == 'n':
            break
    '''    

    '''
    if response['status_code'] == 34:
        return None
    else:
        pass 
    '''
    key = config.TMDB_API_KEY
    url_src_mov = 'https://api.themoviedb.org/3/search/movie?api_key=' + str(key) + '&language=ko-KR&query=' + title   
    resp_src = requests.get(url_src_mov).json()            
    
    if resp_src['total_pages'] == 0:
        return None
    
    rslt_src = resp_src['results']        
    
    lst_ids = []
    
    for dict in rslt_src:
        lst_ids.append(dict['id'])

    tlt_lst = []

    for ids in lst_ids:
        url_rec_mov = 'https://api.themoviedb.org/3/movie/' + str(ids) + '/recommendations?api_key=' + str(key) + '&language=ko-KR'
        resp_rec = requests.get(url_rec_mov).json()  
        
        if 'status_code' in resp_rec.keys():
            return None

        if resp_rec['total_pages'] == 0:
            continue
        
    
        rslt_rec = resp_rec['results'][0]['title']
        tlt_lst.append(rslt_rec)
    
    return tlt_lst

         

    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    제목에 해당하는 영화가 있으면 해당 영화의 id를 기반으로 추천 영화 목록 구성
    추천 영화가 없을 경우 []를 반환
    영화 id 검색에 실패할 경우 None을 반환
    (주의) 추천 영화의 경우 아래 예시 출력과 차이가 있을 수 있음
    """
    pprint(recommendation('기생충'))
    # ['조커', '1917', '조조 래빗', ..생략.., '살인의 추억', '펄프 픽션']
    pprint(recommendation('그래비티'))
    # []
    pprint(recommendation('검색할 수 없는 영화'))
    # None
