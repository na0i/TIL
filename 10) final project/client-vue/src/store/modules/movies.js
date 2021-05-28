import axios from "axios";
// import _ from 'lodash'
// 장고 서버 url
import DRF from '@/api/drf'
import router from "@/router";


const state = {
  genreList: [],
  // movies: [],
  movieList: [],
  recommendMovie: {
    topRated: [],
    popular: [],
    korean: [],  // 한국 영화 평점순
    classic: [],
  },

  // 영화 선택
  selectedMovie: {},
  selectedMovieProviders: {
        buy: [],
        flatrate: [],
        rent: [],
      },

  // 검색 결과
  searchResults: [],
}


const getters = {

  // 유저가 좋아요 누른 영화인지 여부
  isMovieLiked(state, getters, rootState) {
    if (state.selectedMovie.like_users) {
      return !!state.selectedMovie.like_users.filter(user => user.id === rootState.accounts.loginUser.id).length
    } else {
      return false
    }
  },
}


const mutations = {
  /// 초기 세팅 ///
  // 장르 목록
  SET_GENRE_LIST: (state, genres) => {
    state.genreList = genres
  },
  // DB 전체 영화 목록
  SET_MOVIE_LIST: (state, movieList) => {
    state.movieList = movieList
  },
  // 초기 화면에 들어가는 추천 영화들..
  SET_TOP_RATED: (state, topRated) => {
    state.recommendMovie.topRated = topRated
  },
  SET_POPULAR: (state, popular) => {
    state.recommendMovie.popular = popular
  },
  SET_KOREAN: (state, korean) => {
    state.recommendMovie.korean = korean
  },
  SET_CLASSIC: (state, classic) => {
    state.recommendMovie.classic = classic
  },
  //^^^ 초기 세팅 ^^^//


  // 영화 디테일 정보
  SET_MOVIE_DETAIL: (state, movie) => {
    // console.log(movie)
    state.selectedMovie = movie
  },
  // 영화 어디서 볼 수 있나
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

  // 검색
  SET_SEARCH_RESULTS(state, results) {
    state.searchResults = results
  }
}


const actions = {
  //// 초기 세팅 ////
  // 1. 전체 영화 목록 불러오기 -> 제목, id만 가지고 있겠다 -> 검색에서 활용
  // 2. 앞에 띄워주는
  //  top_rated
  //  popularity
  //  한국영화
  //  고전영화
  fetchInitialDatum({commit}) {
    // 2. 초기 화면 추천 영화
    axios.get(DRF.URL + DRF.ROUTES.initial)
      .then(res => {
        commit('SET_TOP_RATED', res.data.data[0])
        commit('SET_POPULAR', res.data.data[1])
        commit('SET_KOREAN', res.data.data[2])
        commit('SET_CLASSIC', res.data.data[3])
      })
      .catch(err => console.log(err))

    // 1. 영화 전체 목록
    axios.get(DRF.URL)
      .then(res => commit('SET_MOVIE_LIST', res.data))
      .catch(err => console.log(err))

    // 전체 장르
    axios.get(DRF.URL + DRF.ROUTES.genres)
      .then(res => commit('SET_GENRE_LIST', res.data))
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

  // 영화 검색
  // ㅎ... url에 담아 보내기 싫어서 그냥 post...
  // 시간 나면 고치겠슴미다..ㅠㅠ
  searchMovie({commit}, query) {
    // 뷰에서 처리해볼까요?
    // let regex = new RegExp('query')
    // // 만족하는 값이 하나라도 있으면 장고로 요청을 보낸다.
    // if ( state.movieList.some(movie => {return regex.test(movie.title)})) {
    //   axios.post(DRF.URL + DRF.ROUTES.search, query)
    //     .then((res) => commit('SET_SEARCH_RESULTS', res.data))
    //     .catch((err) => console.log(err))
    // } else {
      // tmdb로 바로 요청 보내기
    const search_url = `https://api.themoviedb.org/3/search/movie?api_key=1f6f8f7d643eea003df9f19e38d13c3d&language=ko-KR&query=${query}&page=1&include_adult=False`
    axios.get(search_url)
      .then((res) => commit('SET_SEARCH_RESULTS', res.data.results))
      .catch(err => console.log(err))
    router.push({ name: 'SearchResults'})
  }
}


export default {
  state, getters, mutations, actions
}