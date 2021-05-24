<template>
  <div>
    <!-- URL : Component = 1 : 1 
    vue-router 기준 /logout URL 을 구성하기 위한 컴포넌트 -->
  </div>
</template>

<script>
import { mapActions } from 'vuex'

export default {
  name: 'LogoutView',
  methods: {
    ...mapActions(['logout'])
  },
  created() {
    this.logout()
  }
}
</script>