<template>
  <div>
    <h1>리뷰 작성</h1>

    <h3>영화 제목 -> {{ selectedMovie.title }} </h3>

    <span>
      <label for="title">Review Title: </label>
      <input v-model="reviewData.title" id="title" type="text" />
    </span>

    <span>
      <label for="rank"> Movie Rank: </label>
      <select id="rank" v-model="reviewData.rank">
        <option value="1">1</option>
        <option value="2">2</option>
        <option value="3">3</option>
        <option value="4">4</option>
        <option value="5">5</option>
      </select>
    </span>

    <div>
      <label for="content">Review Content: </label>
      <textarea v-model="reviewData.content" id="content" cols="30" rows="10"></textarea>
    </div>

    <div>
      <button @click="createReview(reviewData)"> 작성 완료 </button>
    </div>

  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";

export default {
  name: "CreateReview",
  data() {
    return {
      reviewData: {
        movie: '',
        title: '',
        content: '',
        rank: 3,
      }
    }
  },
  methods: {
    ...mapActions(['createReview']),
  },
  computed: {
    ...mapState({selectedMovie: state => state.movies.selectedMovie}),
    ...mapGetters(['getMovieId'])
  },
  mounted() {
    if (this.getMovieId) {
      this.reviewData.movie = this.getMovieId
    }
  }
}
</script>

<style scoped>

</style>