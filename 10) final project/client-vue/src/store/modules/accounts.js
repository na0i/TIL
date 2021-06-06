import cookies from 'vue-cookies'
import DRF from '@/api/drf.js'
import axios from 'axios'
import router from '@/router'
import _ from "lodash";


const state = {
  authToken: cookies.get('auth-token'),
  loginUser: cookies.get('login-user'),
  recByUser: [],
}

const getters = {
  isLoggedIn: state => !!state.authToken,
  config: state => ({ headers: { Authorization: `Token ${state.authToken}` } })
}

const mutations = {
  SET_TOKEN(state, token) {
    state.authToken = token
  },
  SET_USER(state, user) {
    state.loginUser = user
  },
  SET_REC_BY_USER(state, data) {
    state.recByUser = data
  }
}

const actions = {
  // 추천
  recommendByUser({commit, state}) {
    const genreId = _.sample(state.loginUser.like_genres)
    axios.get(DRF.URL + `genres/${genreId}/`)
      .then((res) => commit('SET_REC_BY_USER', res.data))
      .catch((err) => console.log(err))
  },

  // login 유저 정보 가져오기
  getLoginUser({commit, getters}) {
    axios.get(DRF.URL + DRF.ROUTES.user, getters.config)
      .then((res) => {
        commit('SET_USER', res.data)
        cookies.set('login-user', res.data, '2d')
      })
      .catch((err) => console.log(err))
  },

  // 프로필 페이지 열면
  profileSetting({dispatch}) {
    dispatch('getLoginUser')
      .then(() => dispatch('recommendByUser'))
  },


  // login
  loginpostAuthData({ commit, dispatch }, { path, data }) {
    const FULL_URL_PATH = DRF.URL + path
    axios.post(FULL_URL_PATH, data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        cookies.set('auth-token', res.data.key, '2d')
        dispatch('getLoginUser')
      })
      .then(() => {
        router.go(-1)
      })
      .catch(err => {
        console.error(err.response.data)
      })
  },


  // signup 하면 profile 등록 페이지로 이동
  signuppostAuthData({ commit, dispatch }, { path, data }) {
    const FULL_URL_PATH = DRF.URL + path
    axios.post(FULL_URL_PATH, data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        cookies.set('auth-token', res.data.key, '2d')
      })
      .then(() => {
        dispatch('getLoginUser')
        router.go(-1)
      })
      .catch(err => {
        console.log(err.response.data)
        console.error(err.response.data)
      })
  },

  signup({ dispatch }, signupData) {
    const info = {
      data: signupData,
      // selected_genres: likeGenres,
      path: DRF.ROUTES.signup
    }
    dispatch('signuppostAuthData', info)
  },

  login({ dispatch }, loginData) {
    const info = {
      data: loginData,
      path: DRF.ROUTES.login
    }
    dispatch('loginpostAuthData', info)
  },

  logout({ getters, commit }) {
    const FULL_URL_PATH = DRF.URL + DRF.ROUTES.logout
    axios.post(FULL_URL_PATH, null, getters.config)
      .then(() => {  // Django DB 테이블에서는 삭제 | cookie, state 에서는 존재
        cookies.remove('auth-token')  // cookie 삭제 | state 에서는 존재
        cookies.remove('login-user')
        commit('SET_TOKEN', '')  // state 에서도 삭제
        commit('SET_USER', '')
      })
      .then(() => router.go(-1))
      .catch(err => console.error(err.response.data))
  },
}

export default {
  state, getters, mutations, actions
}
