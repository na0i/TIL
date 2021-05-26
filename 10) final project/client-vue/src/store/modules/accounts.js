import cookies from 'vue-cookies'
import DRF from '@/api/drf.js'
import axios from 'axios'
import router from '@/router'


const state = {
  authToken: cookies.get('auth-token'),
  loginUser: cookies.get('login-user'),
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
  }
}

const actions = {
  // login 유저 정보 가져오기
  getLoginUser({commit, getters}) {
    axios.get(DRF.URL + DRF.ROUTES.user, getters.config)
      .then((res) => {
        commit('SET_USER', res.data)
        cookies.set('login-user', res.data, '2d')
      })
      .catch((err) => console.log(err))
  },

  // login 하면 list 페이지로 이동
  loginpostAuthData({ commit, dispatch }, { path, data }) {
    const FULL_URL_PATH = DRF.URL + path
    axios.post(FULL_URL_PATH, data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        cookies.set('auth-token', res.data.key, '2d')
        dispatch('getLoginUser')
        router.push({ name: 'List' })
      })
      .catch(err => {
        console.error(err.response.data)
      })
  },
  // signup 하면 profile 등록 페이지로 이동 
  signuppostAuthData({ commit }, { path, data }) {
    const FULL_URL_PATH = DRF.URL + path
    axios.post(FULL_URL_PATH, data)
      .then(res => {
        commit('SET_TOKEN', res.data.key)
        cookies.set('auth-token', res.data.key, '2d')
        // logout 하고 profile 추가 작성하기
        cookies.remove('auth-token')
        commit('SET_TOKEN', null)
        router.push({ name: 'Profile' })
      })
      .catch(err => {
        console.error(err.response.data)
      })
  },

  signup({ dispatch }, signupData) {
    const info = {
      data: signupData,
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
        commit('SET_TOKEN', null)  // state 에서도 삭제
        commit('SET_USER', null)
        router.push({ name: 'Profile' }) 
      })
      .catch(err => console.error(err.response.data))
  },
}

export default {
  state, getters, mutations, actions
}
