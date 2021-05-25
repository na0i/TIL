<template>
  <div>
    <h1> Review Detail </h1>
    <h3>
      영화 제목: {{ review.movie.title }}
    </h3>

    <h3>
      리뷰 제목: {{ review.title }}
      평가 : {{ review.rank }}
    </h3>

    <h4>
      리뷰 내용: {{ review.content }}
      <br>
      작성일: {{ review.created_at }}
    </h4>

    <hr>

    <h3>댓글</h3>
    <div @keyup.enter="createComment(commentData)">
      <input v-model="commentData.content"/>
      <button @click="createComment(commentData)" class="btn btn-success">댓글 달기</button>
    </div>

    <ul>
      <li v-for="(comment, idx) in review.comment_set" :key="idx">
        {{ comment }}
      </li>
    </ul>



  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from "vuex";

export default {
  name: "ReviewDetail",
  data() {
    return {
      commentData: {
        movie: '',
        review: '',
        reply_to: '',
        content: '',
      }
    }
  },
  methods: {
    ...mapActions(['createComment'])
  },
  computed: {
    ...mapState({review: state => state.boards.selectedReview}),
    ...mapGetters(['getMovieId', 'getReviewId'])
  },
  mounted() {
    if (this.getMovieId) {
      this.commentData.movie = this.getMovieId
    }
    if (this.$store.getters.getReviewId) {
      this.commentData.review = this.getReviewId
    }
  }
}
</script>

<style scoped>

</style>