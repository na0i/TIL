<template>
  <div>
    <div v-if="isLoggedIn">

      <div v-if="isEdit">
        <input v-model="comment.content" @keyup.enter="[updateComment(commentData), updateRequested()]">
        <button @click="[updateComment(commentData), updateRequested()]"> 수정 완료 </button>
      </div>
      <div v-else class="d-inline-block">
        <div class="comment"> ↪ {{ comment.content }}</div>
      </div>

    <div class="d-inline-block">
      <div v-if="comment.user === $store.state.accounts.loginUser.id" class="d-inline-block">
        <span @click="onClick" class="btn btn-create ms-3">[ 답글 달기</span>
        <span @click="editClicked" class="btn btn-update"> 댓글 수정</span>
        <span @click="deleteClicked" class="btn btn-delete">댓글 삭제 ]</span>
      </div>
      <div v-else class="d-inline-block btn-update">
        <span @click="onClick" class="btn btn-create ms-3">[ 답글 달기 ]</span>
      </div>
    </div>
      <!-- 대댓글 달기 -->
      <div v-if="isClicked">
        <input v-model="commentData.content" @keyup.enter="[createNestedComment(commentData), onSubmit()]">
        <button @click="[createNestedComment(commentData), onSubmit()]"> 등록 </button>
      </div>
      <!-- 대댓글 보여주기 -->
      <div v-if="!!comment.replied_by.length" class="ms-4">
        <div v-for="(comment, idx) in comment.replied_by" :key="idx" class="cocomment">
           <CommentItem :comment="comment"/>
        </div>
      </div>

    </div>
  </div>
</template>

<script>
import {mapActions, mapGetters} from "vuex";

export default {
  name: "CommentItem",
  props: {
    comment: Object
  },
  data() {
    return {
      isClicked: false,
      isEdit: false,
      commentData: {
        movie: '',
        review: '',
        reply_to: '',
        content: '',
      },
    }
  },
  methods: {
    ...mapActions(['createNestedComment', 'updateComment']),
    onClick() {
      this.isClicked = !this.isClicked
    },
    onSubmit() {
      this.isClicked = !this.isClicked
      this.commentData.content = ''
    },
    editClicked() {
      this.isEdit = true
      this.commentData['comment'] = this.comment
    },
    updateRequested() {
      this.isEdit = false
      delete this.commentData['comment']
    },
    deleteClicked() {
      if (confirm('정말 삭제하시겠습니까?')) {
        this.commentData['comment'] = this.comment
        this.$store.dispatch('deleteComment', this.commentData)
        delete this.commentData['comment']
      }
    },
  },
  computed: {
    ...mapGetters(['isLoggedIn']),
  },
  mounted() {
    this.commentData.movie = this.$route.params.movie_id
    this.commentData.review = this.$route.params.review_id
    this.commentData.reply_to = this.comment.id
  },
}
</script>

<style scoped>
.comment {
  font-weight: 380;
}

.btn-create {
  font-size: 14px;
  border-radius: 2px;
  color: aliceblue;
  background-color: transparent;
}

.btn-update {
  font-size: 14px;
  border-radius: 2px;
  background-color: transparent;
}

.btn-delete {
  font-size: 14px;
  border-radius: 2px;
  background-color: transparent;
}

.btn {
  color: rgb(117, 117, 117);
  transition-duration: 0.3s;
  align-content: center;
}

.btn:hover {
  color: white;
  border: 2px solid #3396f4;
}

.cocomment {
  /* background-color: rgb(37, 37, 37); */
  color: #acd7ff;
}

</style>