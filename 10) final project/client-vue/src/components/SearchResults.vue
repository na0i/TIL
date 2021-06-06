<template>
  <div>
    <hr><hr><hr><hr>
    <div class="container ms-4 mt-5">
      <h1 class="bold description">검색 결과</h1>
    <!--</div>-->
    <!--<div class="container">-->
      <li class="row row-cols-6 mt-4">
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
  color: white;
}

</style>