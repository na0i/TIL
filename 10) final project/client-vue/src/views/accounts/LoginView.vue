<template>
  <div class="login container-fluid">
    <div class="row no-gutter">
        <!-- The image half -->
        <div class="col-md-6 d-none d-md-flex bg-image"></div>
          <!-- The content half -->
          <div class="col-md-6 bg-light" style="height: 100vh">
              <div class="login d-flex align-items-center py-5">
                  <!-- Demo content-->
                  <div class="container">
                      <div class="row">
                          <div class="col-lg-10 col-xl-7 mx-auto">
                              <h3 class="fw-bold mt-5">SSATCHA</h3>
                              <p class="text-muted mb-3">LOGIN</p>
                              <form class="accounts-form">
                                <div class="form-group mb-3">
                                    <input id="username" type="text" v-model="loginData.username" placeholder="ID" class="form-control border-0 shadow-sm px-4 text-primary" required="">
                                    <span v-if="validationError.username" class="validation ms-1">
                                      아이디를 입력해주세요.
                                    </span>
                                </div>
                                <div class="form-group mb-3">
                                    <input id="password" type="password" v-model="loginData.password" placeholder="password" class="form-control border-0 shadow-sm px-4 text-primary" required="">
                                    <span v-if="validationError.password" class="validation ms-1">
                                        비밀번호를 입력해주세요.
                                      </span>
                                </div>
                                <div v-if="validationError.non_field_errors" class="validation ms-1">
                                  입력하신 정보와 일치하는 아이디 혹은 비밀번호가 존재하지 않습니다.
                                  <br>
                                  확인 후 다시 입력해주세요.
                                  <br><br>
                                </div>
                                <button type="submit" @click="onClick($event)" class="btn-sm btn-block btn-outline-primary col-12 mb-2 px-5 clickbtn">LOGIN</button>
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
import {mapActions, mapState} from 'vuex'

export default {
  name: 'LoginView',
  data() {
    return {
      loginData: {
        username: null,
        password: null,
      },
    }
  },
  methods: {
    ...mapActions(['login']),
    onClick(event) {
      event.preventDefault()
      this.login(this.loginData)
    }
  },
  computed: {
    ...mapState({
      validationError: state => state.accounts.validationError
    }),
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

.validation {
  color: red;
  font-family: 'Noto Sans KR', sans-serif;
  font-size: 10px;
}
</style>
