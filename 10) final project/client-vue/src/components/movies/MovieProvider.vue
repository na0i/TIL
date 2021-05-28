<template>
  <div class="d-inline-block my-1 me-4 provider">
    <div>

      <a href="" target="_blank" @click.prevent="crawlingProvider(crawlingData)">
      <!--<a href="" target="_blank" @click.prevent="onClick">-->
        <img :src="fullpath" :alt="provider.provider_name" width="40px" height="40px">
      </a>
      {{provider.provider_name}}
    </div>

  </div>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "MovieProvider",
  props: {
    provider: Object,
    method: String
  },
  data() {
    return{
      crawlingData: {
        movie: this.$route.params.movie_id,
        method: this.method,
        provider: this.provider.provider_name,
      },
      url: this.selectedProviderLink,
    }
  },
  methods: {
    ...mapActions(['crawlingProvider']),
    // onClick() {
    //   window.open('https://www.naver.com', '_blank')
    // }
  },
  computed: {
    ...mapState(['selectedProviderLink']),
    fullpath() {
      return "https://image.tmdb.org/t/p/original" + this.provider.logo_path
    },
  },
  watch: {
    url: function (val) {
      console.log('changed')
      window.open(val)
    }
  }
}
</script>

<style scoped>
.provider {
  position: relative;
  z-index: 101;
}
</style>