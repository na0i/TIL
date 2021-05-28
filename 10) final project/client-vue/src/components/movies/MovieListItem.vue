<template>
  <div class="main-container">
    <div class="movie-list pt-2 mb-5">
      <div class="movie-card" @click="setMovieDetail(movie.id)">
        <RouterLink :to="`/${movie.id}`" class="card-text movietitle">
          <img :src="fullpath" alt="movieposter"/>
          <div class="desc mt-1">
            <span class="fw-bolder">{{ movie.title }}</span>
            <br>
            <p class="card-context justify-content:space-between">
              <span>{{ movie.vote_average }}</span>     |     
              <span>{{ movie.release_date }}</span>
            </p>
          </div>
        </RouterLink>
      </div>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "MovieListItem",
  props: {
    movie: Object
  },
  computed: {
    fullpath(){
      return "https://image.tmdb.org/t/p/original/" + this.movie.poster_path
    }
  },
  methods: {
    ...mapActions(['setMovieDetail']),
    onClick() {
      this.$router.push(`/${this.movie.id}`)
    }
  },
}
</script>

<style scoped>
#bg-color {
  background-color: black;
}

/* font css 시작 */
.movietitle {
  font-size: 15px;
  color: #ffffff;
  text-decoration: none;
  text-align: left;
}
/* font css 끝 */

/* card css 시작 */
#card-bg {
  background-color: #b2d7fa;
}

/* * {
  box-sizing: border-box;
} */

.main-container {
  background-color: black;
}

.movie-list {
  flex-wrap: nowrap;
  justify-content: center;
}

.card-context {
  font-size: 12px;
}

.movie-card {
  position: relative;
  align-items: center;
  justify-content: center;
  border-radius: 3px;
  box-shadow: -1px 1px 4px #111111, 1px -1px 4px #111111;
  transition: all 0.5s;
  transition-duration: 300ms;
  height: 200px;
}

.movie-card img {
  transition-duration: 300ms;
  border-radius: 3px 3px 0 0;
  width: 100%;
  height: 100%;
}

.movie-card:hover {
  background-color: #363636;
  box-shadow: -1px 1px 10px 1px #363636, 1px -1px 10px 1px #363636;
}
.movie-card:hover img {
  filter: brightness(50%);
}
/* card css 끝 */
</style>