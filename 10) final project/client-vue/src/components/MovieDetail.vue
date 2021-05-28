<template>
  <div id="moviedetail">
    <img class=backdrop :src="full_backdroppath" width="100%" />
    <br><br><br>
    <div class="container-fluid">
      <div class="row">
        <img :src="full_posterpath" class="col-3 ms-3 poster"/>
        <div class="col-8">
          <h1 class="bold description">{{ movies.selectedMovie.title }}</h1>
          <span class="content pt-1">{{ movies.selectedMovie.original_title }}</span>
          <hr>
          <div class="sm-content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1">평점 : {{ movies.selectedMovie.vote_average }}</span>
          </div>
          <div class="sm-content content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">장르 : 
            <span class="content pt-1" v-for="(genre, idx) in movies.selectedMovie.genres" :key="idx">{{genre.name}}  </span>
          </div>
          <div class="sm-content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1 pe-5">개봉일 : {{ movies.selectedMovie.release_date }}</span>
          </div>
          <br>
          <div class="sm-content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1">줄거리<br>{{ movies.selectedMovie.overview }}</span>
          </div>
        </div>
      </div>

      <hr>

      <div class="row">
        <!-- 사이트 연결 -->
        <div class="col-6">
            <div>
              <div class="sm-content">
                <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">스트리밍 : |
                <span v-for="(provider, idx) in movies.selectedMovieProviders.flatrate" :key="idx" style="text-transform:uppercase">{{provider.provider_name}} | </span>
              </div>
            </div>
            <div>
              <div class="sm-content">
                <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">구매하기 : |
                <span v-for="(provider, idx) in movies.selectedMovieProviders.buy" :key="idx" style="text-transform:uppercase">{{provider.provider_name}} | </span>
              </div>
            </div>
            <div>
              <div class="sm-content">
                <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">대여하기 : |
                <span v-for="(provider, idx) in movies.selectedMovieProviders.rent" :key="idx" style="text-transform:uppercase">{{provider.provider_name}} | 
                </span>
              </div>
            </div>
        </div>


        <div class="col-6">
          <!-- 로그인했으면 리뷰작성 -->
          <div v-if="isLoggedIn">
            <div v-if="isMovieLiked" @click="likeMovie(movies.selectedMovie.id)" >
              <!-- <img src="@/assets/LOGO_black.png" width="25vh" class="ms-2 me-2 dislikebtn"> -->
              이 영화 별로에요
              <img src="@/assets/LOGO_black.png" width="25vh" class="ms-2 me-5 sm-content dislikebtn">
            </div>
            <div v-else @click="likeMovie(movies.selectedMovie.id)" >
              <!-- <img src="@/assets/LOGO_red.png" width="25vh" class="ms-2 me-2 likebtn"> -->
              이 영화 좋아요
              <img src="@/assets/LOGO_red.png" width="25vh" class="ms-2 me-5 sm-content likebtn">
            </div>
            <div class="review-router mt-1">
              <span class="me-3">이 영화에 대한 리뷰 쌓기</span>
              <RouterLink :to="`/${movies.selectedMovie.id}/review/`"><img src="@/assets/LOGO_VER1.png" width="25vh"></RouterLink>
            </div>
          </div>
          <!-- 아니라면 로그인 페이지로 보내기 -->
          <div v-else>
            <h5 class="review-alert"> 영화에 리뷰를 작성하거나 영화를 쌓으시려면 <a href="/accounts/login">로그인</a>하세요!</h5>
          </div>
        </div>
      </div>

      <hr>
      <!-- 리뷰 보여주기 -->
      <ul v-if="reviews.length">
        <h2> 리뷰 </h2>
        <li v-for="(review, idx) in reviews" :key="idx" @click="fetchReview(movies.selectedMovie.id, review.id)">
          <RouterLink :to="`/${movies.selectedMovie.id}/review/${review.id}/`">
            {{ review }}
          </RouterLink>
        </li>
      </ul>
      
    </div>
  </div>
</template>

<script>
import {mapActions, mapState, mapGetters} from "vuex";

export default {
  name: "MovieDetail",
  methods: {
    ...mapActions(['likeMovie']),
    fetchReview(movie, review) {
      this.$store.dispatch('fetchReview', { movie: movie, review: review})
    },
  },
  computed: {
    ...mapState(['movies']),
    ...mapGetters(['isMovieLiked', ]),
    ...mapGetters(['isLoggedIn']),
    reviews() {
      if (this.movies.selectedMovie.reviews === undefined) {
        return []
      } else {
      return this.movies.selectedMovie.reviews
      }
    },
    full_backdroppath() {
      return "https://image.tmdb.org/t/p/original/" + this.movies.selectedMovie.backdrop_path
    },
    full_posterpath() {
      return "https://image.tmdb.org/t/p/original/" + this.movies.selectedMovie.poster_path
    },
  },
}
</script>

<style scoped>
#moviedetail {
  font-family: 'Noto Sans KR', sans-serif;
  color: aliceblue;
}

.backdrop {
  position: absolute;
  opacity: 0.2;
  z-index: 1;
  margin-top: 60px;
}

.description {
  z-index: 1;
}

.content {
  font-weight: 100;
}

.poster {
  z-index: 100;
}

.sm-content {
  vertical-align: middle;
  font-weight: 100;
  font-size: 15px
}

.review-alert {
  font-weight: 100;
  font-size: 15px;
}

.likebtn {
  position: relative;
  z-index: 100;
}

.dislikebtn {
  position: relative;
  z-index: 100;
}

.review-router {
  position: relative;
  z-index: 101;
}
</style>