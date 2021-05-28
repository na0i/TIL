<template>
  <div>
    <h1>Profile</h1>

    <div v-if="isLoggedIn">
      로그인 ok
        <h3>여기는 이제 프로필 다 만들었을 때 보이는 화면</h3>
        -> 닉네임이랑, 좋아요 누른 리뷰, 좋아요 누른 영화 목록 보여주고,
        -> 그거에 기반한 추천 대충 몇가지..
      <br>
      닉네임: {{ loginUser.nickname }}
      <br>
      username: {{ loginUser.username}}
      <hr>
      작성한 리뷰: {{ loginUser.my_reviews }}
      <hr>
      좋아한 영화 : {{ loginUser.like_movies }}
      <hr>
      좋아한 리뷰 : {{ loginUser.like_reviews }}



    </div>
    <div v-else>
      로그인 안 함
    </div>


  </div>
</template>

<script>
import {mapActions, mapGetters, mapState} from 'vuex'

export default {
  name: 'ProfileView',
  methods: {
    ...mapActions(['getLoginUser'])
  },
  computed: {
    ...mapGetters(['isLoggedIn', ]),
    ...mapState({loginUser: state => state.accounts.loginUser})
  },
  created() {
    // 그냥 가지고만 있으면, 프로필 들어올 때마다 처음 받아본 데이터만 가지고 있네요
    // 매번 업데이트 해주겠습니다.
    this.getLoginUser()
  }
}
</script>

<style>
</style>