<template>
  <div>
    <h1> Movie Detail </h1>

    <RouterLink :to="`/${movies.selectedMovie.id}/review/`" class=" btn btn-primary"> 리뷰 작성 </RouterLink>

    <span v-if="isMovieLiked">
      <button @click="likeMovie(movies.selectedMovie.id)" class="btn btn-secondary"> 좋아요 취소 </button>
    </span>
    <span v-else>
      <button @click="likeMovie(movies.selectedMovie.id)" class="btn btn-danger"> 좋아요 </button>
    </span>
    <hr>

    <h3>
      {{ movies.selectedMovie.title }}
    </h3>

    <div>
      구매: {{ movies.selectedMovieProviders.buy }}
    </div>
    <div>
     스트리밍: {{ movies.selectedMovieProviders.flatrate }}
    </div>
    <div>
      대여: {{ movies.selectedMovieProviders.rent }}
    </div>

    <hr>

    <h2> 리뷰 </h2>

    <ul v-if="reviews.length">
      <li v-for="(review, idx) in reviews" :key="idx" @click="fetchReview(movies.selectedMovie.id, review.id)">
        <RouterLink :to="`/${movies.selectedMovie.id}/review/${review.id}/`">
          {{ review }}
        </RouterLink>
      </li>
    </ul>

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
    ...mapGetters(['isMovieLiked']),
    reviews() {
      if (this.movies.selectedMovie.reviews === undefined) {
        return []
      } else {
      return this.movies.selectedMovie.reviews
      }
    }
  },
}
</script>

<style scoped>

</style>