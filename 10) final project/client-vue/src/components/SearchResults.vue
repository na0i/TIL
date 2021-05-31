<template>
  <div>
    <div class="container">
      <h1 class="bold description">검색 결과</h1>
    </div>
    <div class="container" style="margin-top: 20vh">
      <li class="row row-cols-6">
        <MovieListItem v-for="movie in this.$store.state.movies.searchResults" :key="`${movie.id}`" :movie="movie"/>
      </li>
    </div>
  </div>
</template>

<script>
// import {mapState} from "vuex";

import MovieListItem from "@/components/movies/MovieListItem";

export default {
  name: "SearchResults",
  components: {
    MovieListItem,
  },
  computed: {
    // ...mapState({searchResults: state => state.movies.searchResults})
  }
}


</script>

<style scoped>

.description {
  z-index: 1;
  margin-top: 50px;
}

</style>