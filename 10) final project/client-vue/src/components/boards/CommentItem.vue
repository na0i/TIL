<template>
  <div>
    <div v-if="isEdit">
      <input v-model="comment.content" @keyup.enter="[updateComment(commentData), updateRequested()]">
      <button @click="updateComment(commentData), updateRequested()"> 수정 완료 </button>
    </div>
    <div v-else>
      {{ comment.content }}
    </div>

    <span>
      <button @click="onClick" class="btn btn-warning"> 댓글 달기 </button>
    </span>

    <div v-if="comment.user === $store.state.accounts.loginUser.id" class="d-inline-block">
      <button @click="editClicked" class="btn btn-info ms-2"> 댓글 수정 </button>
      <button @click="deleteClicked" class="btn btn-dark ms-2"> 댓글 삭제 </button>
    </div>

    <div v-if="isClicked">
      <input v-model="commentData.content" @keyup.enter="[createNestedComment(commentData), onSubmit()]">
      <button @click="[createNestedComment(commentData), onSubmit()]"> 등록 </button>
    </div>


    <ul v-if="!!comment.replied_by.length" class="ms-5">
      <li v-for="(comment, idx) in comment.replied_by" :key="idx">
        <CommentItem :comment="comment"/>
      </li>
    </ul>

  </div>
</template>

<script>
import {mapActions} from "vuex";

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
  mounted() {
    this.commentData.movie = this.$route.params.movie_id
    this.commentData.review = this.$route.params.review_id
    this.commentData.reply_to = this.comment.id
  },
}
</script>

<style scoped>

</style>