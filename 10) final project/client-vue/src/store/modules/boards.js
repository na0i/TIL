import axios from "axios";
import router from "@/router";
import DRF from '@/api/drf'

const state = {
  reviews: [],
  selectedReview: '',
}

const getters = {
  getReviewId() {
    return state.selectedReview.id
  },
  articles(state) {
    return state.articles
  }
}

const mutations = {
  SET_REVIEW: (state, reviewData) => state.selectedReview = reviewData
}


const actions = {
  // 리뷰 업데이트
  fetchReview({commit}, {movie, review}) {
    console.log(movie, review)
    axios.get(DRF.URL + `${movie}/review/${review}/`)
      .then(res => {
        commit('SET_REVIEW', res.data)
      })
      .catch(err => console.log(err))
  },

  // 새로운 리뷰 생성
  createReview({getters, commit}, reviewData) {
    // <int:movie_pk>/review/
    axios.post(DRF.URL + `${reviewData.movie}/review/`, reviewData, getters.config)
      .then((res) => {commit('SET_REVIEW', res.data)})
        // router.push({path: `/${res.data.movie.id}/review/${res.data.id}`})
      .then(() => router.push({ name: 'ReviewDetail', params: {movie_id: reviewData.movie, review_id: this.state.boards.selectedReview.id}}))
      .catch(err => console.log(err))
  },

  // 새로운 댓글 작성
  createComment({getters, dispatch}, commentData) {
    console.log(getters)
    // console.log(commit)
    console.log(commentData)
  //   <int:movie_pk>/review/<int:review_pk>/comment/
    axios.post(DRF.URL + `${commentData.movie}/review/${commentData.review}/comment/`, commentData, getters.config)
      // 댓글 생성에 성공하는 경우, review data 전체를 그냥 새로 불러오면 되지 않을 까 싶어요
      .then(() => dispatch('fetchReview', { movie: commentData.movie, review: commentData.review}))
  }
}

export default {
  state, getters, mutations, actions
}
