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
                                    <input id="username" type="text" v-model="signupData.username" placeholder="username" required="" class="form-control border-0 shadow-sm px-4 text-primary">
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
                                <button type="submit" @click="signup(signupData)" class="btn-sm btn-block btn-outline-primary col-12 mb-2 px-5 clickbtn">WELCOME to SSATCHA WORLD!</button>
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
        password1: '',
        password2: '',
        email: '',
        nickname: '',
        selected_genres: [],
      },
    }
  },
  methods: {
    ...mapActions(['signup']),
    ...mapState({genreList: state => state.movies.genreList}), // ?? 왜 안대?
    onSelect(likeGenres) {
      this.signupData.selected_genres = likeGenres
    }
  }
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
