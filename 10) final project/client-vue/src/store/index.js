import Vue from 'vue'
import Vuex from 'vuex'

import accounts from './modules/accounts'
import movies from "@/store/modules/movies";
import boards from "@/store/modules/boards";

// import createPersistedState from "vuex-persistedstate";

Vue.use(Vuex)

export default new Vuex.Store({
  modules: {accounts, movies, boards, },

  // plugins: [createPersistedState()],

})
