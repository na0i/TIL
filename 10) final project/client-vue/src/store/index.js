import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import movies from "@/store/modules/movies";
import boards from "@/store/modules/boards";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: { accounts, movies, boards, }
})
