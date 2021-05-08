## PJT 09

#### 1. 참여자

박나영, 정우기



#### 2. 구현

##### 2 - 1)팔로우

JS의 addeventlister와 axios를 통해서 form tag를 클릭할 시 팔로우 기능이 새로고침없이 동작할 수 있도록 구현하였다.

##### 2 - 2)좋아요

JS의 addeventlister와 axios를 통해서 form tag를 클릭할 시 좋아요 기능이 새로고침없이 동작할 수 있도록 구현



##### 2 - 3)추천 알고리즘

- 아이디어

  ```
  넷플릭스 참고
  - 인기컨텐츠
  - 수상작
  - 최근 시청 카테고리의 영화 추천
  - 시청한 컨텐츠 기반 유사 컨텐츠
  ```

  

- 실제로 구현하려고 했던 것

  ```
  - 팔로우하는 유저의 리뷰를 상위 랭킹 순으로 정렬해 해당 영화 가져오기
  - 팔로우하는 유저가 좋아요 누른 리뷰의 영화와 비슷한 장르
  ```



- 실제 구현한 것

  ```python
  @login_required # 로그인한 사용자만 접근 가능
  @require_GET
  def recommended(request):
      # 요청 보낸 사람이 팔로우하고 있는 사람 가져오기
      follow_users = request.user.followings.all()
      movies_list = []
      for follow_user in follow_users:
          # 리뷰를 rank가 높은 순으로 가져오기
          reviews = follow_user.like_reviews.order_by('rank')
          # 한 사람당 약 3개 정도 가져오기(영화 제목)
          for i in range(3):
              movies_list.append(reviews[i].movie_title)
      
      # 한 유저 당 3개씩 영화를 가져오는데 만약 그 수가 10개가 넘는다면
      # random shuffle 후 10개만 slicing해 가져오기
      if len(movies_list) > 10:
          random.shuffle(movies_list)
          movies_list = movies_list[0:10]
      context = {
          'movies_list': movies_list,
      }
      return render(request, 'movies/recommended.html', context)
  ```

  

##### 2 - 4) pjt09를 통해 알게 된 점

- local host 주소 설정: 127.0.0 이런식으로 주소를 설정하면 안된다.

  ```html
  axios({
  method: 'post',
  url: `http://localhost:8000/community/${reviewId}/like/`,
  headers: {'X-CSRFToken': csrftoken},
  })
  ```



- 좋아요 버튼의 색 변경

  항상 `좋아요`, `좋아요 취소`와 같은 형태로 버튼을 구성했었는데 이번 프로젝트에서는 좋아요 버튼은 빨강색, 취소 버튼은 검정색이 되도록 구현해 보았다.

  - button이 아니라 i 태그에 접근하기 위해서 i 태그에 `id = "btnIcon-{{ review. pk }}"` 로 id를 설정
  - const icon을 통해 reviewId를 이용하여 i 태그 선택
  - icon.style로 색상 변경

  ```html
  <button class="btn btn-link" id="like-{{ review.pk }}">
  <i id="btnIcon-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:crimson;"></i>
  </button>
  {% else %}
  <button class="btn btn-link" id="like-{{ review.pk }}">
  <i id="btnIcon-{{ review.pk }}" class="fas fa-heart fa-lg" style="color:black;"></i>
  </button>
  
  // 생략 //
  
  const likeButton = document.querySelector(`#like-${reviewId}`)
  const icon = document.querySelector(`#btnIcon-${reviewId}`)
  if (liked) {
  icon.style = 'color:crimson'
  } else {
  icon.style= 'color:black'
  }
  ```

  

#### 3. 소감

알고리즘을 배우면서 알고리즘이 현업에 어떻게 사용되는지 감이 잘 오지 않았었습니다. 알고리즘을 그저 수학 문제와 같다고 생각했었습니다. 그래서 '유튜브 알고리즘이 여기로 이끌었다' 라는 말을 들을 때마다 내가 배운 알고리즘과 무슨 관련이 있는것인지 궁금했습니다. 하지만 이번 PJT를 통해 웹의 작은 기능들 조차도 알고리즘으로 구현되었다는 것을 깨달았습니다. 