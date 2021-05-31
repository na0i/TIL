<template>
  <div>
    <p>Profile</p>

    <div v-if="isLoggedIn" class="profile">
      <div class="container mt-5">
        <br>
        <div id="semititle" class="fw-bolder m-3">안녕하세요  {{ loginUser.nickname }}님!</div>
        <!--<br>-->
        <!--<div class="profile">username: {{ loginUser.username}}</div>-->
        <hr>
        
        <div>
          <span id="semititle" class="fw-bolder m-3">쌓은 리뷰들: </span>
          <div v-for="review in loginUser.my_reviews" :key="`r${review.id}`" @click="fetchReview(review.movie.id, review.id)" class="h3 mt-3 ms-3">
            <RouterLink :to="`/${review.movie.id}/review/${review.id}/`" class="text-decoration-none h2">
              {{ review.title }}
            </RouterLink>
          </div>
        </div>

        <hr>

        <div>
          <span id="semititle" class="fw-bolder m-3">좋아한 리뷰:</span>
          <div v-for="review in loginUser.like_reviews" :key="`r${review.id}`" @click="fetchReview(review.movie.id, review.id)" class="h3 mt-3 ms-3">
            <RouterLink :to="`/${review.movie.id}/review/${review.id}/`" class="text-decoration-none h2">
              {{ review.title }}
            </RouterLink>
          </div>
        </div>
        
        <hr>
        
        <div>
          <span id="semititle" class="fw-bolder m-3">쌓인 영화들:</span>
            <li class="row row-cols-6">
              <MovieListItem v-for="movie in loginUser.like_movies" :key="`m${movie.id}`" :movie="movie"/>
            </li>
            <!--<li v-for="movie in like_movies" :key="`m${movie.id}`" :movie="movie">-->
            <!--  {{ loginUser.like_movies }}-->
            <!--</li>-->
        </div>

        <hr>

      <div class="container" >
        <h2 id="semititle" class="fw-bolder m-3">{{ loginUser.nickname }} 님이 좋아하실만한 영화를 추천해드려요!</h2>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in recByUser" :key="movie.id" :movie="movie"/>
        </li>
      </div>
    </div>
  </div>


    <div v-else>
      로그인 안 함
    </div>

  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'
import MovieListItem from "@/components/movies/MovieListItem";

export default {
  name: 'ProfileView',
  components: {
    MovieListItem
  },
  methods: {
    ...mapActions(['profileSetting']),
    fetchReview(movie, review) {
      this.$store.dispatch('fetchReview', { movie: movie, review: review})
    },
  },
  computed: {
    ...mapGetters(['isLoggedIn', ]),
    ...mapState({
      loginUser: state => state.accounts.loginUser,
      recByUser: state => state.accounts.recByUser,
    })
  },
  created() {
    // 그냥 가지고만 있으면, 프로필 들어올 때마다 처음 받아본 데이터만 가지고 있네요
    // 매번 업데이트 해주겠습니다.
    this.profileSetting()
    // this.getLoginUser()
  }
}
</script>

<style scoped>
#semititle {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 22px;
  color: white;
  text-align: left;
}

.profile {
  position: relative;
  z-index: 99;
  color: white;
}

.ssatchareview {
  text-decoration: none;
}
</style>