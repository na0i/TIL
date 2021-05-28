<template>
  <div id="app">
    <nav class="nav navbar navbar-expand-lg">
      <div class="container-fluid">
        <a class="navbar-brand" href="/">
          <img src="@/assets/LOGO_KOR.png" alt="LOGO_KOR" width="168" height="35" class="d-inline-block ms-1 align-self-center">

          <span class="ms-4">
            <span class="ms-5">
              <RouterLink v-if="!isLoggedIn" :to="{ name: 'Signup' }">SIGNUP</RouterLink>
            </span>
            <span class="ms-5">
              <RouterLink v-if="!isLoggedIn" :to="{ name: 'Login' }">LOGIN</RouterLink>
            </span>
            <RouterLink v-if="isLoggedIn" :to="{ name: 'Logout' }">LOGOUT | </RouterLink>
            <RouterLink v-if="isLoggedIn" :to="{ name: 'Profile' }">PROFILE |</RouterLink>
          </span>
        </a>

          <div >
            <SearchBar/>
          </div>
      </div>
    </nav>
    <RouterView/>
  </div>
</template>

<script>
import {mapActions, mapGetters} from 'vuex'
import SearchBar from "@/components/SearchBar";

export default {
  name: 'App',
  components: {
    SearchBar
  },
  computed: {
    ...mapGetters(['isLoggedIn', ]),
    ...mapActions(['fetchInitialDatum'])
  },
  created() {
    this.fetchInitialDatum
  }
}
</script>

<style scoped>
.nav {
  position: absolute;
  z-index: 15;
  width: 100%;
  vertical-align: middle;
}

.nav a {
  color: #b7d1eb;
  text-decoration: none;
  font-size: 18px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; 
  /* 텍스트가 렌더링될 때 부드럽게 표현 */
  -moz-osx-font-smoothing: grayscale; 
}


</style>
