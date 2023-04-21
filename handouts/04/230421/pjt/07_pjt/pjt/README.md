07_PJT_서울1반_서동훈
-----------
# DB 설계를 활용한 REST API 설계
1. mypjt 를 장고로 스타트한 뒤 movies앱을 만들어준다
  
2. Avtor, Movie, Review 3가지 모델을 models.py에 정의해준 뒤 각각의 필드들을 저장해준다.
   
3. 필드들을 정의해줄 때 ERD(Entity-Relationship Diagram)를 보면서 각각 필드에 필요한 데이터 유형을 지정해준다. 
   
4. admin site에 각각의 모델을 등록해 admin site에서 데이터의 조회 생성 수정 삭제가 가능하도록 한다.
   
5. serializers.py 차일을 movies앱내에 만들어 준 뒤 ERD(Entity-Relationship Diagram)과 요구사항에 명시된 view함수들을 보면서 해당 함수들이 작동할 수 있도록 중개테이블을 만들어준다.
   - 먼저 각각 모델에 해당하는 serializer 클래스들을 정의해 준 뒤 view함수에서 디테일하게 요구하는 사항들에 필요한 class들을 추가로 더 만들어주도록 하였다. 
     - ex) actor_detail 함수에서는 단일 배우 정보인 이름만 제공하지만 출연 영화 제목 또한 포함시키기 위해 ActorDetailSerializer라는 클래스를 새로 만들어 그 안에 우선적으로 MovieSerializer를 다시 정의해준뒤 필요한 필드인 영화제목인 'title'만 받아준다. 그 후 ActorDetailSerializer의 Meta클래스를 다시 정의해 주고 해당 클래스에서 요구하는 필드인 영화제목인 타이틀을 위에서 정의해준 MovieSerializer로 재정의해주는 식으로 영화제목을 가져왔다. 물론 이때 Movie모델에서 actors라는 필드를 ManyToManyField로 받아주어 위에 작업이 가능하도록 했다.  

  
6. 명세서에서 요구하는 함수들을 각각의 Method에 따라 view에 정의해준다.

7. 모델과 view와 serializer들을 모두 정의해 줬으면 마이그래이션을 진행해 준 뒤 제공된 fixture파일을 받아 해당 json파일들을 등록시켜준다.

8. 위에 view함수들을 만들어 줄 때 해당 함수를 실행시킬 경로인 url역시 지정해주었다.
   
9. 서버를 킨 뒤 postman을 키고 해당 url에 들어가 데이터들을 조작, 조회, 수정, 삭제등을 해본다.


### 처음에는 수월하게 진행되었지만 중간에 중개테이블을 만들고 참조, 역참조의 관계가 조금 헷갈려 serializer 클래스를 새로 만들어주는 단계에서 시간을 조금 잡아먹었다. 해당 코드가 정확한 지는 모르겠지만 요구하는 동작은 오류없이 진행되니 뭐..


07_PJT_서울1반_이성우
--------------
# DB 설계를 활용한 REST API 설계

## 학습 내용
- Django 및 DRF를 활용하여 REST API를 설계하는 방법을 중점적으로 학습함.
- 이를 통해, JSON 자료를 자유롭게 다루고, 추후 있을 관통프로젝트에 적용하고자 함.

## 어려웠던 부분
- ERD(Entity-Relationship Diagram)을 확인하며 M:N 모델 구조 관계를 정의하는 것에 어려움을 느낌 
- 또한, 앞서 정의한 모델 관계를 활용하여 serializer에 필드를 추가/삭제하는 과정에서 숙련이 필요하다고 느낌
  - 아직 해결하지 못 한 어려움 
    - serializer와 필드의 관계를 정확히 모르겠음
    - model간 참조/역참조 관계에 대해 심도깊은 이해가 필요함.
      - 예를 들어) related_name 과 serializer 필드명 간 관계 등 
    - 정확한 필드 추가/삭제 로직을 이해하지 못함
- 추후 serializer-model relationship에 대한 심도깊은 이해를 통해 자유자재로 DB를 설계하고자 함


## 새로 배운 것들
- Django를 통해 JSON을 표시할 때 모델의 필드 내에 또다른 필드를 내포할 수 있음을 배움.
- ForeignKey 혹은 ManyToMany 관계로 모델 간 연결되어 있다면, 연결된 모델의 id를 title 혹은 actor_name과 같은 내재 데이터로 표현할 수 있음.


## 느낀점
- Django로 백엔드를 설계할 때 모델 간 관계 설정이 매우 중요하다고 느낌
- 초보적인 백엔드 설계 단에서, 데이터 필드를 유연하게 조작하는 것이 매우 중요하다고 느낌.
- 캐시, 트래픽과 같은 고급 설계는 부차적인 문제
- 그러므로 관통 프로젝트 전까지 데이터 조작을 유연하게 하자는 목표를 설정함.
- 동훈이와의 페어 프로그래밍은 재밌다.
- 다음 페어 프로그래밍도 행복하게 마무리하기