import axios from "axios";
import _ from 'lodash'
// 장고 서버 url
import DRF from '@/api/drf'


const state = {
  movies: [],
  selectedMovie: {},
  selectedMovieProviders: {
        buy: [],
        flatrate: [],
        rent: [],
      },
}


const getters = {
  fetchTopRated() {
    return _.sortBy(state.movies.filter(movie => movie.vote_count > 300), 'vote_average').reverse().slice(0, 40)
  },
  fetchPopularity() {
    return _.sortBy(state.movies, 'popularity').reverse().slice(0, 40)
  },
  fetchKorean() {
    // 한국 영화 중에서 평점 높은 순 40개
    return _.sortBy(state.movies.filter(movie => movie.original_language === 'ko'), 'vote_average').reverse().slice(0, 40)
  },
  fetchClassic() {
    // 70~ 80 년대 영화 추천
    return _.sortBy(state.movies.filter(movie => {
      let regex = new RegExp('^197|^198')
      return regex.test(movie.release_date)}, 'vote_average').reverse().slice(0, 40)
    )
  },

  // 유저가 좋아요 누른 영화인지 여부
  isMovieLiked(state, getters, rootState) {
    if (state.selectedMovie.like_users) {
      return !!state.selectedMovie.like_users.filter(user => user.id === rootState.accounts.loginUser.pk).length
    } else {
      return false
    }
  },
}


const mutations = {
  SET_MOVIES: (state, movies) => {
    state.movies = movies
  },
  SET_MOVIE_DETAIL: (state, movie) => {
    // console.log(movie)
    state.selectedMovie = movie
  },
  SET_PROVIDERS: (state, data) => {
    if (data === undefined) {
      state.selectedMovieProviders.buy = []
      state.selectedMovieProviders.flatrate = []
      state.selectedMovieProviders.rent = []
    } else {
      if (data.buy) {
        state.selectedMovieProviders.buy = data.buy
      }
      if (data.flatrate) {
        state.selectedMovieProviders.flatrate = data.flatrate
      }
      if (data.rent) {
        state.selectedMovieProviders.rent = data.rent
      }
    }
  },

  // 좋아요 누른 유저 저장
  SET_MOVIE_LIKE_USERS(state, likeUsers) {
    state.selectedMovie.like_users = likeUsers
  },
}


const actions = {
  // 초기 영화 데이터 가져오기
  fetchMovies({commit}) {
    axios.get(DRF.URL)
      .then(res => {
        commit('SET_MOVIES', res.data)
      })
      .catch(err => console.log(err))
  },

  // 저장된 영화 정보 -> 리뷰 및 좋아요까지
  fetchMovieDetail({commit}, movieId) {
    axios.get(DRF.URL + `${movieId}/`)
      .then((res) => commit('SET_MOVIE_DETAIL', res.data))
      .catch((err) => console.log(err))
  },

  // 선택한 영화 상세정보 불러오기
  setMovieDetail({dispatch, commit}, movieId) {
    dispatch('fetchMovieDetail', movieId)
    axios.get(`https://api.themoviedb.org/3/movie/${movieId}/watch/providers?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&page=1`)
    .then(res => { commit('SET_PROVIDERS', res.data.results.KR)})
    .catch(err => console.log(err))
  },

  // 영화 좋아요
  likeMovie({getters, commit, rootState}, movie) {
    const loginUser = rootState.accounts.loginUser
    axios.post(DRF.URL + `${movie}/likes/`, loginUser, getters.config)
      .then((res) => commit('SET_MOVIE_LIKE_USERS', res.data.like_users))
      .catch((err) => console.log(err))
  },
}


export default {
  state, getters, mutations, actions
}