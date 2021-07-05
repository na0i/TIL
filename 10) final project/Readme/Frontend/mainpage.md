### 메인페이지 CSS

-------

##### [영화 보여주기]

container에 row-cols-6을 주어 반응형 css를 구현하였다.(한줄에 영화 6개씩)



##### [영화 개수]

state에서 영화를 가져와 `.slice`를 이용하여

NowPlaying과 TopRated는 12개씩, Popularity, Korean Movies, Classic은 6개씩 가져왔다.

id는 movie_id를 이용해 v-for문을 사용하였고, 영화 세부페이지로 이동할 수 있도록 props를 사용하였다.