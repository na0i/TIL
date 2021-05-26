<template>
  <div>
    <h1> Review Detail </h1>
    <h3 class="d-inline-block">
      영화 제목:
    </h3>
      <div @click="setMovieDetail(review.movie.id)" class="h3 d-inline-block">
        <RouterLink :to="`/${review.movie.id}`">
           {{ review.movie.title }}
        </RouterLink>
      </div>

    <h3>
      리뷰 제목: {{ review.title }}
      평가 : {{ review.rank }}
    </h3>

    <h4>
      리뷰 내용: {{ review.content }}
      <br>
      작성일: {{ review.created_at }}
      <br>
      수정일: {{ review.updated_at }}
    </h4>

    <span v-if="isReviewLiked">
      <button @click="likeReview(commentData)" class="btn btn-secondary"> 리뷰 좋아요 취소 </button>
    </span>
    <span v-else>
      <button @click="likeReview(commentData)" class="btn btn-danger"> 리뷰 좋아요 </button>
    </span>

    <hr>

    <div v-if="review.user === $store.state.accounts.loginUser.pk">
      <button @click="editReview" class="btn btn-info ms-2"> 리뷰 수정 </button>
      <button @click="deleteReview(review)" class="btn btn-dark ms-2"> 리뷰 삭제 </button>
    </div>


    <hr>

    <h3>댓글</h3>
    <div >
      <input v-model="commentData.content" @keyup.enter="[createComment(commentData), onSubmit()]"/>
      <button @click="[createComment(commentData), onSubmit()]" class="btn btn-success">댓글 달기</button>
    </div>

    <div v-if="isCommented">
      <ul>
        <li v-for="(comment, idx) in notNestedComments" :key="idx">
          <CommentItem :comment="comment"/>
        </li>
      </ul>
    </div>

  </div>
</template>

<script>
import {mapActions, mapGetters, mapState } from "vuex";
import CommentItem from "@/components/boards/CommentItem";

export default {
  name: "ReviewDetail",
  components: {
    CommentItem,
  },
  data() {
    return {
      review: {
        movie: {
          id: '',
          title: '',
        },
      },
      commentData: {
        movie: '',
        review: '',
        reply_to: '',
        content: '',
      }
    }
  },
  methods: {
    ...mapActions(['createComment', 'fetchReview', 'likeReview', 'setMovieDetail']),
    onSubmit() {
      this.commentData.content = ''
    },
    editReview() {
      this.$router.push({ name: 'UpsertReview', params: { isUpdate: true, movie_id: this.commentData.movie, review: this.review }})
    },
    deleteReview() {
      if (confirm('정말 삭제하시겠습니까?')) {
        this.$store.dispatch('deleteReview', this.review)
      }
    },
  },
  computed: {
    ...mapState({selectedReview: state => state.boards.selectedReview}),
    ...mapGetters(['isReviewLiked', 'notNestedComments', 'getMovieId']),
    isCommented() {
      return !!this.review.comment_set;
    },
  },
  watch: {
    '$store.state.boards.selectedReview': function() {
        this.review = this.selectedReview
    }
  },
  created() {
    this.commentData.movie = this.$route.params.movie_id
    this.commentData.review = this.$route.params.review_id
    if (this.selectedReview) {
      this.review = this.selectedReview
    }
  },

}
</script>

<style scoped>

</style>