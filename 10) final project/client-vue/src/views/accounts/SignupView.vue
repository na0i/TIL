<template>
  <div class="container-fluid">
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
                            <h3 class="fw-bold">SSATCHA</h3>
                            <p class="text-muted mb-3">CREATE ACCOUNT</p>
                            <form class="accounts-form">
                                <div class="input-box form-group mb-1 pb-1">
                                    <input id="username" type="text" v-model="signupData.username" placeholder="ID" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                    <!--<span v-if="usernameError">-->
                                    <!--  {{ this.errorMessage.username }}-->
                                    <!--</span>-->
                                </div>
                                <div class="form-group mb-1 pb-1">
                                      <input id="nickname" type="text" v-model="signupData.nickname" placeholder="nickname" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-1 pb-1">
                                    <input id="email" type="email" v-model="signupData.email" placeholder="email" required="" autofocus="" class="form-control border-0 shadow-sm px-4">
                                </div>
                                <div class="form-group mb-1 pb-1">
                                    <input id="password1" type="password" v-model="signupData.password1" placeholder="password" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="form-group mb-1 pb-1">
                                    <input id="password2" type="password" v-model="signupData.password2" placeholder="confirm password" required="" class="form-control border-0 shadow-sm px-4 text-primary">
                                </div>
                                <div class="button-set mt-2 mb-2 ">
                                  <SignupGenreSelect @like-genres="onSelect"/>
                                </div>
                                <button type="submit" @click="onClick($event)" class="btn-sm btn-block btn-outline-primary col-12 mb-2 px-5 clickbtn">WELCOME to SSATCHA WORLD!</button>
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
import SignupGenreSelect from "@/components/accounts/SignupGenreSelect";

export default {
  name: 'SignupView',
  components: {
    SignupGenreSelect
  },
  data() {
    return {
      signupData: {
        username: '',
        nickname: '',
        email: '',
        password1: '',
        password2: '',
        selected_genres: [],
      },
      errorMessage: {
        username: '',
        nickname: '',
        email: '',
        password1: '',
        password2: ''
      }
    }
  },
  methods: {
    ...mapActions(['signup']),
    onSelect(likeGenres) {
      this.signupData.selected_genres = likeGenres
    },
    onClick(event) {
      // 이거 해주지 않으면 페이지가 새로고침되면서 Bad pipe 에러가 발생합니다.
      event.preventDefault()
      this.signup(this.signupData)
    }
  },
  computed: {
    ...mapState({
      validationError: state => state.accounts.validationError
    }),
    // usernameError() {
    //   if (this.validationError.username) {
    //     if (this.validationError.username.includes('10')) {
    //       this.errorMessage.username = '아이디는 10자까지 설정 가능합니다.'
    //     } else if (this.validationError.username.includes('numeric')) {
    //       this.errorMessage.username = '숫자로만 이루어진 아이디는 사용하실 수 없습니다.'
    //     } else if (this.errorMessage.username.includes('short')) {
    //       this.errorMessage.username = '아이디가 너무 짧습니다.'
    //     } else {
    //       this.errorMessage.username = this.validationError.username
    //     }
    //     return true
    //   } else {
    //     return false
    //   }
    // }
  },
}
</script>

<style scoped>
.signup-ft {
  font-family: 'Noto Sans KR', sans-serif;
  color: white;
  font-size: 23px;
}

.img-box {
  max-width: 100%;
}

.login,
.image {
  min-height: 100vh;
}

.bg-image {
  height: 100vh;
  background-image: url("../../assets/accounts_bg.jpg");
  background-size: cover;
  background-position: center;
  /*스크롤 무관하게 이미지 고정*/
  position: sticky;
  top: 0;
}

.input-box {
  font-size: 13px;
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
