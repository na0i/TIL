<template>
  <div class="login container-fluid">
    <div class="row no-gutter">
        <!-- The image half -->
        <div class="col-md-6 d-none d-md-flex bg-image"></div>
          <!-- The content half -->
          <div class="col-md-6 bg-light">
              <div class="login d-flex align-items-center py-5">
                  <!-- Demo content-->
                  <div class="container">
                      <div class="row">
                          <div class="col-lg-10 col-xl-7 mx-auto">
                              <h3 class="fw-bold mt-5">SSATCHA</h3>
                              <p class="text-muted mb-3">LOGIN</p>
                              <form class="accounts-form">
                                <div class="form-group mb-3">
                                    <input id="username" type="text" v-model="loginData.username" placeholder="username" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-3">
                                    <input id="password1" type="password" v-model="loginData.password1" placeholder="password" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="button-set">
                                  <SignupGenreSelect @like-genres="onSelect"/>
                                </div>
                                <button type="submit" @click="login(loginData)" class="btn-sm btn-block btn-outline-primary col-12 mb-2 px-5 clickbtn">SIGN UP</button>
                              </form>
                          </div>
                      </div>
                  </div><!-- End -->
              </div>
          </div><!-- End -->
        </div>
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      }
    }
  },
  methods: {
    ...mapActions(['login'])
  }
}
</script>

<style scoped>
.bg-image {
  height: 100vh;
  background-image: url("../../assets/accounts_bg.jpg");
  background-size: cover;
  background-position: center;
}

.login {
  font-family: 'Noto Sans KR', sans-serif;
}

.button-set {
  background: #d6eaff;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 13px;
}

.click-btn {
  background: #3396f4;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 15px;
}
</style>
