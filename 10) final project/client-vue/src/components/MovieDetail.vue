<template>
  <div>
    <h1> Movie Detail </h1>

    <RouterLink :to="`/${movies.selectedMovie.id}/review/`" class=" btn btn-primary"> 리뷰 작성 </RouterLink>

    {{ movies.selectedMovie }}
    <div>
      구매: {{ movies.selectedMovieProviders.buy }}
    </div>
    <div>
     스트리밍: {{ movies.selectedMovieProviders.flatrate }}
    </div>
    <div>
      대여: {{ movies.selectedMovieProviders.rent }}
    </div>
  </div>
</template>

<script>
import {mapState} from "vuex";

export default {
  name: "MovieDetail",
  actions:{
  },
  computed: {
    ...mapState(['movies'])
  },
}
</script>

<style scoped>

</style>