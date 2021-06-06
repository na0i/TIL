<template>
  <div id="bg-color">
    <div id="carouselExampleCaptions" class="carousel slide" data-bs-ride="carousel">
      <div class="carousel-indicators">
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="0" class="active" aria-current="true" aria-label="Slide 1"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="1" aria-label="Slide 2"></button>
        <button type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide-to="2" aria-label="Slide 3"></button>
      </div>
      <div class="carousel-inner">
        <div class="carousel-item active">
          <img src="@/assets/interstella.jpg" class="d-block w-100" height="100%" alt="interstella_poster">
          <!--<a href="">-->
          <div class="carousel-caption d-none d-md-block">
            <div class="mb-5 pb-3">
              <h2 class="fw-bolder">I N T E R S T E L L A R</h2>
              <span class="carousel-font">" We will find a way. We always have. "</span>
            </div>
          <!--</a>-->
            <div>
              <a href="https://www.youtube.com/watch?v=d2VN6NNa9BE" class="carousel-font fw-bold">
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
                WATCH TRAILER
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
              </a>
            </div>
            <div class="mt-5 mb-2">
              <span class="carousel-actor-font"> Matthew McConaughey  |  Jessica Chastain  |  Anne Hathaway </span>
                <br>
              <span class="carousel-actor-font"> Michael Caine  |  Casey Affleck  |  Mackenzie Foy </span>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/joker.jpg" class="d-block w-100" height="100%" alt="joker_poster">
          <div class="carousel-caption d-none d-md-block">
            <div class="mb-5 pb-3">
              <h2 class="fw-bolder">J O K E R</h2>
              <span class="carousel-font">" I thougt my life was a tragedy, but it was a fuckking comedy. "</span>
            </div>
            <div>
              <a href="https://www.youtube.com/watch?v=EXeTwQWrcwY" class="carousel-font fw-bold">
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
                WATCH TRAILER
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
              </a>
            </div>
            <div class="mt-5 mb-2">
              <span class="carousel-actor-font"> Joaquin Phoenix  |  Robert De Niro  |  Zazie Beetz </span>
                <br>
              <span class="carousel-actor-font"> Frances Conroy  |  Brett Cullen  |  Shea Whigham </span>
            </div>
          </div>
        </div>
        <div class="carousel-item">
          <img src="@/assets/frozen.jpg" class="d-block w-100" height="100%" alt="frozen2_poster">
          <div class="carousel-caption d-none d-md-block">
            <div class="mb-5 pb-3">
              <h2 class="fw-bolder">F R O Z E N 2</h2>
              <span class="carousel-font">" I just thought of one thing that's permanent. 'Love' "</span>
            </div>
            <div>
              <a href="https://www.youtube.com/watch?v=EXeTwQWrcwY" class="carousel-font fw-bold">
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
                WATCH TRAILER
                <img src="@/assets/LOGO_VER1.png" width="30" height="30" class="mb-2">
              </a>
            </div>
            <div class="mt-5 mb-2">
              <span class="carousel-actor-font"> Kristen Bell  |  Idina Menzel  |  Josh Gad </span>
            </div>
          </div>
        </div>
      </div>
      <button class="carousel-control-prev" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="prev">
        <span class="carousel-control-prev-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Previous</span>
      </button>
      <button class="carousel-control-next" type="button" data-bs-target="#carouselExampleCaptions" data-bs-slide="next">
        <span class="carousel-control-next-icon" aria-hidden="true"></span>
        <span class="visually-hidden">Next</span>
      </button>
    </div>
    <div class="container">
      <p id="semititle" class="fw-bolder mt-3">TOP RATED</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in topRated.slice(0,12)" :key="`${movie.id}`" :movie="movie"/>
        </li>
      </div>
    
      <p id="semititle" class="fw-bolder mt-5">POPULARITY</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in popular.slice(0,6)" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.popularity }}  -->
        </li>
      </div>

      <p id="semititle" class="fw-bolder mt-5">KOREAN MOVIES</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in korean.slice(0,6)" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.vote_average }} -->
        </li>
      </div>

      <p id="semititle" class="fw-bolder mt-5">고전 명작</p>
      <div>
        <li class="row row-cols-6">
          <MovieListItem v-for="movie in classic.slice(10,16)" :key="`${movie.id}`" :movie="movie"/>
          <!-- {{ movie.release_date }} -->
        </li>
      </div>
      <br><br>
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";
import MovieListItem from "@/components/movies/MovieListItem";

export default {
  name: "MovieIndex",
  components: {
    MovieListItem,
  },
  data() {
    return {
      movieId: '',
    }
  },
  methods: {
    onClick() {
      this.$router.push(`/${this.movieId}`)
    }
  },
  computed: {
    ...mapState({
      topRated: state => state.movies.recommendMovie.topRated,
      popular: state => state.movies.recommendMovie.popular,
      korean: state => state.movies.recommendMovie.korean,
      classic: state => state.movies.recommendMovie.classic
    }),
  },
}
</script>

<style scoped>
#title {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 30px;
  color: #b7d1eb;
}

#semititle {
  /* font-family: Noto Sans KR, sans-serif; */
  font-size: 22px;
  color: white;
  text-align: left;
}

#bg-color {
  background-color: black;
}

/* carousel */
.carousel-item {
  height: 100vh;
  background: no-repeat center center scroll;
  -webkit-background-size: cover;
  -moz-background-size: cover;
  -o-background-size: cover;
  background-size: cover;
}


.carousel-font {
  font-size: 15px;
  text-align: right;
  text-decoration: none;
  color: rgb(255, 255, 255);
}

.carousel-actor-font {
  font-size: 12px;
  text-align: right;
  text-decoration: none;
  color: rgb(207, 207, 207);
}

.flux {
  font-family: neon;
  color: #3396f4;
  text-shadow: 0 0 0vw #07143f;
}

.flux {
  animation: flux 2s linear infinite;
  -moz-animation: flux 2s linear infinite;
  -webkit-animation: flux 2s linear infinite;
  -o-animation: flux 2s linear infinite;
}

@keyframes flux {
  0%,
  100% {
    text-shadow: 0 0 1vw #3396f4, 0 0 3vw #3396f4, 0 0 10vw #3396f4, 0 0 10vw #3396f4, 0 0 .4vw #242d35, .5vw .5vw .1vw #0d151d;
    color: #28D7FE;
  }
  50% {
    text-shadow: 0 0 .5vw #082180, 0 0 1.5vw #082180, 0 0 5vw #082180, 0 0 5vw #082180, 0 0 .2vw #082180, .5vw .5vw .1vw #0A3940;
    color: #146C80;
  }
}
</style>