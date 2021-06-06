<template>
  <div id="app">
    <NavBar/>
    <div>
      <RouterView/>
    </div>
  </div>
</template>

<script>
import {mapActions} from 'vuex'
import NavBar from "@/views/NavBar";

export default {
  name: 'App',
  components: {
    NavBar,
  },
  computed: {
    ...mapActions(['fetchInitialDatum']),

  },
  created() {
    this.fetchInitialDatum
  }
}
</script>

<style scoped>
.nav {
  position: absolute;
  z-index: 100;
  width: 100%;
  vertical-align: middle;
}

.nav a {
  color: #b7d1eb;
  text-decoration: none;
  /*font-weight: bolder;*/
  font-size: 18px;
}

#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased; 
  /* 텍스트가 렌더링될 때 부드럽게 표현 */
  -moz-osx-font-smoothing: grayscale; 
}

</style>
