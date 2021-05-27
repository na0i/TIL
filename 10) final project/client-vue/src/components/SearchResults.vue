<template>
  <div>
    <h1>검색 결과</h1>
    <MovieListItem v-for="movie in this.$store.state.movies.searchResults" :key="`${movie.id}`" :movie="movie"/>
    {{ this.$store.state.movies.searchResults }}
    {{ searchResults }}
  </div>
</template>

<script>
// import {mapState} from "vuex";

import MovieListItem from "@/components/MovieListItem";

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

</style>