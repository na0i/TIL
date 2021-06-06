<template>
  <div>
    <!--로그인 및 회원가입 -->
    <nav v-if="needHide" class="nav navbar navbar-expand-lg container-fluid d-flex justify-content-between align-items-end m-2">
      <a class="navbar-brand ms-2 d-block" href="/">
        <img src="@/assets/LOGO_KOR.png" alt="LOGO_KOR" width="168" height="35" class="ms-1 align-self-center">
      </a>
    </nav>
    <nav v-else class="nav navbar navbar-expand-lg container-fluid d-flex justify-content-between align-items-end m-2">
      <!--<div class="container-fluid d-flex justify-content-between align-items-end m-2">-->
        <div class="d-inline-flex align-items-end">

        <a class="navbar-brand ms-2 d-block" href="/">
          <img src="@/assets/LOGO_KOR.png" alt="LOGO_KOR" width="168" height="35" class="ms-1 align-self-center">
        </a>

          <div class="d-inline-block mx-5">
            <span v-if="!isLoggedIn">
              <RouterLink :to="{ name: 'Signup' }">SIGNUP</RouterLink>
            </span>
            <span v-if="!isLoggedIn" class="ms-5">
              <RouterLink :to="{ name: 'Login' }">LOGIN</RouterLink>
            </span>
            <span v-if="isLoggedIn">
              <RouterLink :to="{ name: 'Profile' }">PROFILE </RouterLink>
            </span>
            <span v-if="isLoggedIn" class="ms-5">
              <RouterLink :to="{ name: 'Logout' }">LOGOUT </RouterLink>
            </span>
          </div>
        </div>
        <div class="w-50">
          <SearchBar/>
        </div>
      <!--</div>-->
    </nav>

  </div>
</template>

<script>
import SearchBar from "@/components/SearchBar";
import {mapGetters} from "vuex";

export default {
  name: "NavBar",
  components: {
    SearchBar,
  },
  computed: {
    ...mapGetters(['isLoggedIn',]),
    // 로그인/ 회원가입에서는 검색창이랑 안보이게
    needHide() {
      return !!(this.$route.name === 'Signup' || this.$route.name === 'Login');
    },
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
</style>