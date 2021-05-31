<template>
  <div>
    <p>r</p>

    <img class="backdrop" :src="full_backdroppath" width="100%">
    <div class="container-fluid reviewdetail">
        <!-- <img src="@/assets/LOGO_VER1.png"> -->
        <br><br><br>
          <div @click="setMovieDetail(review.movie.id)" class="h3 d-inline-block">
            <RouterLink :to="`/${review.movie.id}`" class="text-decoration-none">
              {{ review.movie.title }}
            </RouterLink>
          </div>

        <div class="about-review">
          <span class="reviewtitle fw-bold">리뷰 제목 : </span>
          <span class="reviewdetail">{{ review.title }}</span>
          <br>
          <span class="reviewtitle fw-bold">평가 : </span>
          <span class="reviewdetail">{{ review.rank }}</span>

          <p class="reviewtitle fw-bold mt-1">리뷰 내용</p>
          <span class="reviewdetail">{{ review.content }}</span>
          
        </div>

          <div align="right">
            <br>
            <span class="datetime">작성일: {{ review.created_at }}</span>
            <br>
            <span class="datetime">수정일: {{ review.updated_at }}</span>
          </div>

        <span v-if="isReviewLiked">
          <button @click="likeReview(commentData)" class="btn btn-secondary"> 리뷰 좋아요 취소 </button>
        </span>
        <span v-else>
          <button @click="likeReview(commentData)" class="btn btn-danger"> 리뷰 좋아요 </button>
        </span>


        <div v-if="review.user === $store.state.accounts.loginUser.pk">
          <button @click="editReview" class="btn btn-info ms-2"> 리뷰 수정 </button>
          <button @click="deleteReview(review)" class="btn btn-dark ms-2"> 리뷰 삭제 </button>
        </div>


        <hr>

        <h3>댓글</h3>
        <div class="comment-input">
          <input class="me-1" v-model="commentData.content" @keyup.enter="[createComment(commentData), onSubmit()]"/>
          <button @click="[createComment(commentData), onSubmit()]" class="btn btn-primary">댓글 달기</button>
        </div>

        <div v-if="isCommented">
          <ul>
            <li v-for="(comment, idx) in notNestedComments" :key="idx">
              <CommentItem :comment="comment"/>
            </li>
          </ul>
        </div>
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
    full_backdroppath() {
      return "https://image.tmdb.org/t/p/original/" + this.review.movie.backdrop_path
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
.reviewdetail {
  position: relative;
  font-family: 'Noto Sans KR', sans-serif;
  color: rgb(255, 255, 255);
  z-index: 99;
  font-weight: 100;
}

.backdrop {
  position: absolute;
  opacity: 0.1;
  z-index: 1;
  margin-top: 60px;
}

.about-review {
  position: relative;
  z-index: 100;
  font-size: 20px;
}

.review-title {
  font-weight: 300;
  font-size: 20px;
}

.date-time {
  font-size: 15px;
  text-align: right;
}

.comment-input {
  vertical-align: middle;
}
</style>