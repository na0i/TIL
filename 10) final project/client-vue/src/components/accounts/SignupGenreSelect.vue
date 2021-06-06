<template>
  <div>
    <ul class="ks-cboxtags d-flex flex-wrap justify-content-around contain">
      <li v-for="(genre, idx) in this.$store.state.movies.genreList" :key="idx">
        <input type="checkbox" v-model="likeGenres" @click="onChange(genre)" :id="`${genre.id}`" :value="genre"><label :for="`${genre.id}`">{{ genre.name }}</label>
      </li>
    </ul>
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
}
</script>

<style scoped>

.contain {
    max-width: 640px;
    font-family: 'Segoe UI', Tahoma, Geneva, Verdana, sans-serif;
    font-size: 13px;
}

ul.ks-cboxtags {
    list-style: none;
    padding: 20px;
}
ul.ks-cboxtags li{
  display: inline;
}
ul.ks-cboxtags li label{
    display: inline-block;
    background-color: rgba(255, 255, 255, .9);
    border: 2px solid rgba(139, 139, 139, .3);
    color: #adadad;
    border-radius: 25px;
    white-space: nowrap;
    margin: 3px 0px;
    -webkit-touch-callout: none;
    -webkit-user-select: none;
    -moz-user-select: none;
    -ms-user-select: none;
    user-select: none;
    -webkit-tap-highlight-color: transparent;
    transition: all .2s;
}

ul.ks-cboxtags li label {
    padding: 8px 12px;
    cursor: pointer;
}

ul.ks-cboxtags li label::before {
    display: inline-block;
    font-style: normal;
    font-variant: normal;
    text-rendering: auto;
    -webkit-font-smoothing: antialiased;
    font-weight: 900;
    font-size: 12px;
    padding: 2px 6px 2px 2px;
    content: "\f067";
    transition: transform .3s ease-in-out;
}

ul.ks-cboxtags li input[type="checkbox"]:checked + label::before {
    content: "\f058";
    transform: rotate(-360deg);
    transition: transform .3s ease-in-out;
}

ul.ks-cboxtags li input[type="checkbox"]:checked + label {
    border: 2px solid  #a6c7ff;
    background-color: #8daee5;
    color: #fff;
    transition: all .2s;
}

ul.ks-cboxtags li input[type="checkbox"] {
  display: absolute;
}
ul.ks-cboxtags li input[type="checkbox"] {
  position: absolute;
  opacity: 0;
}
ul.ks-cboxtags li input[type="checkbox"]:focus + label {
  border: 2px solid #8daee5;
}


/*input[type=checkbox] {*/
/*  appearance: none;*/
/*  width: 40px;*/
/*  height: 16px;*/
/*  border: 1px solid #aaa;*/
/*  border-radius: 2px;*/
/*  background: #ebebeb;*/
/*  position: relative;*/
/*  display: inline-block;*/
/*  overflow: hidden;*/
/*  vertical-align: middle;*/
/*  transition: background 0.3s;*/
/*  box-sizing: border-box;*/
/*}*/

/*input[type=checkbox]:after {*/
/*  content: "";*/
/*  position: absolute;*/
/*  top: -1px;*/
/*  left: -1px;*/
/*  width: 14px;*/
/*  height: 14px;*/
/*  background: white;*/
/*  border: 1px solid #aaa;*/
/*  border-radius: 2px;*/
/*  transition: left 0.1s cubic-bezier(0.785, 0.135, 0.15, 0.86);*/
/*}*/

/*input[type=checkbox]:checked {*/
/*  background: #a6c7ff;*/
/*  border-color: #8daee5;*/
/*}*/

/*input[type=checkbox]:checked:after {*/
/*  left: 23px;*/
/*  border-color: #8daee5;*/
/*}*/
</style>