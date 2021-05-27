<template>
  <div>
    <div class="input-group">
      <input class="form-control" v-model="query">
      <button class="btn btn-close-white" @click="onClick"> Go! </button>
    </div>
  </div>
</template>

<script>
import {mapActions} from "vuex";

export default {
  name: "SearchBar",
  data() {
    return {
      query: '',
    }
  },
  methods: {
    ...mapActions(['searchMovie']),
    onClick() {
      this.searchMovie(this.query)
    }
  }
}
</script>

<style scoped>

</style>