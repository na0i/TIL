<template>
  <div id="moviedetail">
    <img class=backdrop :src="full_backdroppath" width="100%" />
    <br><br><br>
    <div class="container-fluid" style="margin-top: 30px">
      <div class="row">
        <img :src="full_posterpath" class="col-3 ms-3 poster"/>
        <div class="col-8">
          <h1 class="bold description">{{ selectedMovie.title }}</h1>
          <span class="content pt-1">{{ selectedMovie.original_title }}</span>
          <hr>
          <div>
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1">평점 : {{ selectedMovie.vote_average }}</span>
          </div>
          <div class="content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">장르 : 
            <span class="content pt-1" v-for="(genre, idx) in selectedMovie.genres" :key="idx">{{genre.name}}  </span>
          </div>
          <div>
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1 pe-5">개봉일 : {{ selectedMovie.release_date }}</span>
          </div>
          <br>
          <div class="sm-content">
            <img src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">
            <span class="content pt-1">줄거리<br>{{ selectedMovie.overview }}</span>
          </div>
        </div>
      </div>

      <hr>

      <div class="row">
        <!-- 사이트 연결 -->
        <div class="col-6">
          <div class="sm-content">
            <div v-if="hasFlatrate">
              <img  src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">스트리밍 : 
              <MovieProvider v-for="provider in this.selectedMovieProviders.flatrate" :key="`f${provider.provider_id}`" :provider="provider" method="flatrate" style="text-transform:uppercase"/>
            </div>

            <div v-if="hasBuy">
              <img  src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">구매하기 : 
              <MovieProvider v-for="provider in this.selectedMovieProviders.buy" :key="`b${provider.provider_id}`" :provider="provider" method="buy" style="text-transform:uppercase"/>
            </div>

            <div v-if="hasRent">
              <img  src="@/assets/LOGO_VER1.png" width="20px" height="20px" class="m-1">대여하기 : 
              <MovieProvider v-for="provider in this.selectedMovieProviders.rent" :key="`r${provider.provider_id}`" :provider="provider" method="rent" style="text-transform:uppercase"/>
            </div>

            <div v-if="isVoid">
              <p>현재 감상할 수 있는 곳이 없어요!</p>
            </div>
            <div v-else>
              <br>
              <p>* 아이콘을 클릭하시면 해당 페이지로 연결됩니다.</p>
            </div>
          </div>
        </div>


        <div class="col-6">
          <!-- 로그인했으면 리뷰작성 -->
          <div v-if="isLoggedIn">
            <div v-if="isMovieLiked" @click="likeMovie(selectedMovie.id)" >
              <!-- <img src="@/assets/LOGO_black.png" width="25vh" class="ms-2 me-2 dislikebtn"> -->
              이 영화 별로에요
              <img src="@/assets/LOGO_black.png" width="25vh" class="ms-2 me-5 sdislikebtn">
            </div>
            <div v-else @click="likeMovie(selectedMovie.id)" >
              <!-- <img src="@/assets/LOGO_red.png" width="25vh" class="ms-2 me-2 likebtn"> -->
              이 영화 좋아요
              <img src="@/assets/LOGO_red.png" width="25vh" class="ms-2 me-5 likebtn">
            </div>
            <br>
            <div class="review-router mt-1">
              <span class="me-3">이 영화에 대한 리뷰 쌓기</span>
              <RouterLink :to="`/${selectedMovie.id}/review/`"><img src="@/assets/LOGO_VER1.png" width="25vh"></RouterLink>
            </div>
          </div>
          <!-- 아니라면 로그인 페이지로 보내기 -->
          <div v-else>
            <h5 class="review-alert review-list"> 영화에 리뷰를 작성하거나 영화를 쌓으시려면 <a href="/accounts/login">로그인</a>하세요!</h5>
          </div>
        </div>
      </div>
      <hr>
      <!-- 리뷰 보여주기 -->
      <ol v-if="reviews.length" class="review-list">
        <div class="align-items-center">
          <img src="@/assets/LOGO_VER1.png" width="25vh" class="mb-1 me-1"><h4 class="d-inline-block"> 쌓인 리뷰 </h4>
        </div>
        <li v-for="(review, idx) in reviews" :key="idx" @click="fetchReview(selectedMovie.id, review.id)" class="h5 mt-3 ms-3">
          <RouterLink :to="`/${selectedMovie.id}/review/${review.id}/`">
            {{ review.title }}
          </RouterLink>
        </li>
      </ol>
      <h3 v-else class="text-center mt-2"> 이 영화의 첫 리뷰를 쌓아주세요!</h3>
    </div>
  </div>
</template>

<script>
import MovieProvider from "@/components/movies/MovieProvider";
import {mapActions, mapState, mapGetters} from "vuex";

export default {
  name: "MovieDetail",
  components: {
    MovieProvider
  },
  data() {
    return {
      movie: {}
    }
  },
  methods: {
    ...mapActions(['likeMovie']),
    fetchReview(movie, review) {
      this.$store.dispatch('fetchReview', { movie: movie, review: review})
    },
  },
  computed: {
    ...mapState({
      selectedMovie: state => state.movies.selectedMovie,
      selectedMovieProviders: state => state.movies.selectedMovieProviders
    }),
    ...mapGetters(['isMovieLiked', ]),
    ...mapGetters(['isLoggedIn']),
    reviews() {
      if (this.selectedMovie.reviews === undefined) {
        return []
      } else {
      return this.selectedMovie.reviews
      }
    },
    full_backdroppath() {
      return "https://image.tmdb.org/t/p/original" + this.selectedMovie.backdrop_path
    },
    full_posterpath() {
      return "https://image.tmdb.org/t/p/original" + this.selectedMovie.poster_path
    },
    hasFlatrate() {
      return !!this.selectedMovieProviders.flatrate.length
    },
    hasBuy() {
      return !!this.selectedMovieProviders.buy.length
    },
    hasRent() {
      return !!this.selectedMovieProviders.rent.length
    },
    isVoid() {
      return this.hasFlatrate || this.hasBuy || this.hasRent ? false : true;
    }
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
  margin-top: 80px;
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

.review-alert {
  font-weight: 100;
  font-size: 15px;
}

.likebtn {
  position: relative;
  z-index: 100;
  cursor: pointer;
}

.dislikebtn {
  position: relative;
  z-index: 100;
  cursor: pointer; 
}

.review-router {
  position: relative;
  z-index: 101;
}

.review-list {
  position: relative;
  z-index: 102;
}
</style>