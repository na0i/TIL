import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import movies from "@/store/modules/movies";
import boards from "@/store/modules/boards";

import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {accounts, movies, boards, },

  plugins: [createPersistedState({
    // 등록되어 있는 값만 저장
    paths: ['movies', 'boards'],
  })],

})
