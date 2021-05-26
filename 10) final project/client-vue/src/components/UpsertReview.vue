<template>
  <div>
    <h1 v-if="isUpdate">리뷰 수정</h1>
    <h1 v-else> 리뷰 작성</h1>

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

    <div v-if="isUpdate">
      <button @click="updateReview(reviewData)"> 수정 완료 </button>
    </div>
    <div v-else>
      <button @click="createReview(reviewData)"> 작성 완료 </button>
    </div>

  </div>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "UpsertReview",
  data() {
    return {
      reviewData: {
        movie: '',
        title: '',
        content: '',
        rank: 3,
      },
    }
  },
  methods: {
    ...mapActions(['createReview', 'updateReview']),
  },
  computed: {
    ...mapState({selectedMovie: state => state.movies.selectedMovie}),
    isUpdate () {
      return this.$route.params.isUpdate
    },
  },
  mounted() {
    this.reviewData.movie = this.$route.params.movie_id
    // 수정인 경우, 기본 데이터값들이 나올 수 있도록
    if (this.$route.params.isUpdate) {
      this.reviewData.title = this.$route.params.review.title
      this.reviewData.content = this.$route.params.review.content
      this.reviewData.rank = this.$route.params.review.rank
      this.reviewData['review'] = this.$route.params.review.id
    }
  }
}
</script>

<style scoped>

</style>