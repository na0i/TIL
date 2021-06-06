import axios from "axios";
import router from "@/router";
import DRF from '@/api/drf'

const state = {
  reviews: [],
  selectedReview: '',
}

const getters = {
  // 좋아요를 누른 리뷰인지 여부
  isReviewLiked(state, getters, rootState ) {
    if (state.selectedReview.like_users) {
      return !!state.selectedReview.like_users.filter(user => user.id === rootState.accounts.loginUser.id).length
    } else {
      return false
    }
  },

  // watch store
  getMovieId: function (state) {
    if (state.selectedReview.movie) {
      return state.selectedReview.movie.id
    } else {
      return null
    }
  },

  // 대댓글 제외 댓글만
  notNestedComments(state) {
    return state.selectedReview.comment_set.filter(comment => comment.reply_to === null)
  }
}

const mutations = {
  // 선택한 리뷰 저장
  SET_REVIEW: (state, reviewData) => state.selectedReview = reviewData,

  // 리뷰 좋아요 유저 목록 업데이트
  SET_REVIEW_LIKE_USERS(state, likeUsers) {
    state.selectedReview.like_users = likeUsers
},

  // 댓글 목록 업데이트
  SET_COMMENT_SET(state, commentSet) {
    state.selectedReview.comment_set = commentSet
  }

}


const actions = {

  // 새로운 리뷰 생성 --> C
  createReview({getters, commit}, reviewData) {
    // <int:movie_pk>/review/
    axios.post(DRF.URL + `${reviewData.movie}/review/`, reviewData, getters.config)
      .then((res) => {commit('SET_REVIEW', res.data)})
      .then(() => router.push({ name: 'ReviewDetail', params: {movie_id: reviewData.movie, review_id: this.state.boards.selectedReview.id}}))
      .catch(err => console.log(err))
  },

  // 리뷰 불러오기 -> R
  fetchReview({commit}, {movie, review}) {
    axios.get(DRF.URL + `${movie}/review/${review}/`)
      .then(res => {
        commit('SET_REVIEW', res.data)
      })
      .catch(err => console.log(err))
  },

  // 리뷰 업데이트 -> U
  updateReview({getters, commit}, reviewData) {
    axios.put(DRF.URL + `${reviewData.movie}/review/${reviewData.review}/`, reviewData, getters.config)
      .then(res => { commit('SET_REVIEW', res.data)})
      .then(() => router.push({ name: 'ReviewDetail', params: {movie_id: reviewData.movie, review_id: reviewData.review}}))
      .catch(err => console.log(err))
  },

  // 리뷰 삭제 -> D
  deleteReview({getters, dispatch, rootState}, review) {
    const loginUser = rootState.accounts.loginUser
    axios.delete(DRF.URL + `${review.movie.id}/review/${review.id}/`, {data: loginUser}, getters.config)
      .then(() => dispatch('fetchMovieDetail', review.movie.id ))
      .then(() => router.push({ name: 'MovieDetail', params: {movie_id: review.movie.id}}))
      .catch(err => console.log(err))
  },


  // 새로운 댓글 작성 -> C
  createComment({getters, dispatch}, commentData) {
  //   <int:movie_pk>/review/<int:review_pk>/comment/
    axios.post(DRF.URL + `${commentData.movie}/review/${commentData.review}/comment/`, commentData, getters.config)
      // 댓글 생성에 성공하는 경우, review data 전체를 그냥 새로 불러오면 되지 않을 까 싶어요
      .then(() => dispatch('fetchReview', { movie: commentData.movie, review: commentData.review}))
      .catch((err) => console.log(err))
  },

  // 대댓글 작성 -> R
  createNestedComment({getters, commit}, commentData) {
    axios.post(DRF.URL + `${commentData.movie}/review/${commentData.review}/comment/${commentData.reply_to}/`, commentData, getters.config)
      .then((res) => commit('SET_COMMENT_SET', res.data.comment_set))
      .catch((err) => console.log(err))
  },

  // 댓글 수정 -> U
  updateComment({getters, commit}, commentData) {
    axios.put(DRF.URL + `${commentData.movie}/review/${commentData.review}/comment/${commentData.comment.id}/`, commentData, getters.config)
      .then(res => commit('SET_COMMENT_SET', res.data.comment_set))
      .catch((err) => console.log(err))
  },

  // 댓글 삭제 -> D
  deleteComment({getters, commit, rootState}, {movie, review, comment}) {
    const loginUser = rootState.accounts.loginUser
    axios.delete(DRF.URL + `${movie}/review/${review}/comment/${comment.id}/`, {data: loginUser}, getters.config)
      .then((res) => commit('SET_COMMENT_SET', res.data.comment_set))
      .catch(err => console.log(err))
  },

  // 리뷰 좋아요
  likeReview({getters, commit, rootState}, {movie, review}) {
    const loginUser = rootState.accounts.loginUser
    axios.post(DRF.URL + `${movie}/review/${review}/likes/`, loginUser, getters.config)
      .then((res) => commit('SET_REVIEW_LIKE_USERS', res.data.like_users))
      .catch((err) => console.log(err))
  },
}

export default {
  state, getters, mutations, actions
}
