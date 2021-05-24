<template>
  <div id="app">
    <div id="navbar navbar-dark bg-dark">
      <RouterLink to="/">SSATCHA</RouterLink> |
      <!-- <RouterLink :to="{ name: 'List' }">Articles</RouterLink> | -->
      <RouterLink v-if="!isLoggedIn" :to="{ name: 'Signup' }">Signup | </RouterLink> 
      <RouterLink v-if="!isLoggedIn" :to="{ name: 'Login' }">Login |</RouterLink> 
      <RouterLink v-if="isLoggedIn" :to="{ name: 'Logout' }">Logout | </RouterLink>
      <RouterLink v-if="isLoggedIn" :to="{ name: 'Profile' }">Profile |</RouterLink>
    </div>
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
  methods: {
    hi() {
      console.log('hi')
    }
  }
}
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
}

#nav {
  padding: 30px;
}

#nav a {
  font-weight: bold;
  color: #2c3e50;
}

#nav a.router-link-exact-active {
  color: #42b983;
}
</style>
