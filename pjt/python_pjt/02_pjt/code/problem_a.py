import requests
import config


def popular_count():
    key = config.TMDB_API_KEY
    URL = 'https://api.themoviedb.org/3/movie/popular?api_key=' + str(key) + '&language=en-US'

    response = requests.get(URL).json()
    rslt_resp = response['results']
    num_pmov = len(rslt_resp)
    return num_pmov


    # 여기에 코드를 작성합니다.  


# 아래의 코드는 수정하지 않습니다.
if __name__ == '__main__':
    """
    popular 영화목록의 개수 반환
    """
    print(popular_count())
    # 20
