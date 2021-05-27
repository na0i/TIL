<template>
  <div class="d-flex flex-wrap justify-content-between">
    
    <div v-for="(genre, idx) in this.$store.state.movies.genreList" :key="idx" class="col-3">
      {{ genre.name }}
      <input type="checkbox" data-toggle="toggle" :data-on="genre.name" :data-off="genre.name" data-onstyle="info" data-offstyle="outline-secondary">
    </div>
        <!--<input type="checkbox" v-model="likeGenres" :value="genre" :id="`${genre.id}`" @click="onChange(genre)" class="btn btn-outline-primary mt-1" autocomplete="off">-->
        <!--{{ genre.name}}-->

    <!--<div v-for="(genre, idx) in this.$store.state.movies.genreList" :key="idx" class="col-3">-->
    <!--  {{ genre.name }}-->
    <!--  <input type="checkbox" v-model="likeGenres" :value="genre" @click="onChange(genre)" class="btn-check mt-1">-->
    <!--</div>-->
    <!-- {{likeGenres}} -->
  </div>
</template>

<script>
export default {
  name: "SignupGenreSelect",
  data() {
    return {
      likeGenres: [],
    }
  },
  methods: {
    // 아 진짜 이거 하나 만드는데 1시간반...
    onChange(justAdded) {
      let idx = this.likeGenres.indexOf(justAdded)
      let changed
      if (idx !== -1) {
        changed = this.likeGenres.splice(idx, 1)
      } else {
        changed = [...this.likeGenres, justAdded]
      }
      this.$emit('like-genres', changed)
    }
  },
  computed: {
  },
  // watch: {
  //   changed: function() {
  //     console.log('here')
  //     const handler = () => {console.log(this.likeGenres); return this.likeGenres}
  //     // 왜 여기서도 한개를 덜 잡아오죵...
  //     console.log('---', handler())
  //     console.log('changed')
  //     this.$emit('like-genre')}
  // }
}
</script>

<style scoped>
input[type=checkbox] {
  appearance: none;
  width: 40px;
  height: 16px;
  border: 1px solid #aaa;
  border-radius: 2px;
  background: #ebebeb;
  position: relative;
  display: inline-block;
  overflow: hidden;
  vertical-align: middle;
  transition: background 0.3s;
  box-sizing: border-box;
}

input[type=checkbox]:after {
  content: "";
  position: absolute;
  top: -1px;
  left: -1px;
  width: 14px;
  height: 14px;
  background: white;
  border: 1px solid #aaa;
  border-radius: 2px;
  transition: left 0.1s cubic-bezier(0.785, 0.135, 0.15, 0.86);
}

input[type=checkbox]:checked {
  background: #a6c7ff;
  border-color: #8daee5;
}

input[type=checkbox]:checked:after {
  left: 23px;
  border-color: #8daee5;
}
</style>