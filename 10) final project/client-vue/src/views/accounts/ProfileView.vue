<template>
  <div>
    <h1>Profile</h1>
      <div v-show = 'isLoggedIn'>
        
      </div>
      <div v-show = '!isLoggedIn'>
        <div>
          <label for="nickname">nickname:</label>
          <input v-model="ProfileData.nickname" id="nickname" type="text" />
        </div>
      </div>
  </div>
</template>

<script>
import { mapGetters } from 'vuex'

export default {
  name: 'ProfileView',
  computed: {
    ...mapGetters(['isLoggedIn', ])
  },
  data() {
    return {
      ProfileData: {
        nickname: null,
        image: null,
      }
    }
  },
}
</script>

<style>
</style>