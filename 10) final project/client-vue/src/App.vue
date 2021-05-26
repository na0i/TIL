<template>
  <div id="app bg-color">
    <nav id = "nav" class="navbar navbar-dark">
      <div class="container">
        <a class="navbar-brand" href="/">
          <img src="@/assets/LOGO_KOR.png" alt="LOGO_KOR" width="168" height="35" class="d-inline-block align-text-top">
        </a>
        <div class="justify-content-center fw-bolder">
          <RouterLink v-if="!isLoggedIn" :to="{ name: 'Signup' }">SIGNUP</RouterLink> |    
          <RouterLink v-if="!isLoggedIn" :to="{ name: 'Login' }">LOGIN</RouterLink>
          <RouterLink v-if="isLoggedIn" :to="{ name: 'Logout' }">LOGOUT | </RouterLink>
          <RouterLink v-if="isLoggedIn" :to="{ name: 'Profile' }">PROFILE |</RouterLink>
        </div>
      </div>
    </nav>
    <RouterView/>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'App',
  computed: {
    ...mapGetters(['isLoggedIn', ])
  },
}
</script>

<style scoped>
#bg-color {
  background-color: black;
  text-align: center;
}

#nav {
  background-color: black;
  padding: 5px;
  color: #b7d1eb;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; 
  /* 텍스트가 렌더링될 때 부드럽게 표현 */
  -moz-osx-font-smoothing: grayscale; 
  text-align: center;
  color: #2c3e50;
}

#nav a {
  color: #3396f4;
  text-decoration: none;
  font-size: 18px;
}

#nav a.router-link-exact-active {
  color: #3396f4;
}
</style>
