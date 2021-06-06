<template>
  <div>
    <div class="upsertreview">

    
      <div class="d-flex justify-content-between align-items-stretch" style="margin-top: 20vh">
        <div>
          <h5 v-if="isUpdate" class="review">리뷰 수정</h5>
          <h5 v-else class="review"> 리뷰 작성</h5>
          <h4 class="review-title">{{ selectedMovie.title }} </h4>
        </div>
      </div>

      <div class="form_group field">
        <input type="text" v-model="reviewData.title" class="form_field" placeholder="Review Title" name="name" id='name' required />
        <label for="name" class="form_label">리뷰 제목을 입력하세요. </label>
      </div>

      <div class="form_group field">
        <textarea v-model="reviewData.content" id="content" rows="5" placeholder="Review Content" content="content" class="form_field" required></textarea>
        <label for="content" class="form_label">리뷰 내용을 입력하세요. </label>
      </div>

      <div class="container d-flex justify-content-center mt-3">


          <div class="mt-5">
            <span v-if="isUpdate">
              <button @click="updateReview(reviewData)" class="button mt-3"> 수정 완료 </button>
            </span>
            <span v-else>
              <button @click="createReview(reviewData)" class="button mt-3"> 작성 완료 </button>
            </span>
          </div>


          <div class="row">
            <div class="col-3">
              <div class="optionbox">
                <select id="rank" v-model="reviewData.rank">
                  <option value="1">1</option>
                  <option value="2">2</option>
                  <option value="3">3</option>
                  <option value="4">4</option>
                  <option value="5">5</option>
                </select>
              </div>
            </div>
          </div>

      </div>
    </div>
  </div>
</template>

<script>
import {mapActions, mapState} from "vuex";

export default {
  name: "UpsertReview",
  data() {
    return {
      reviewData: {
        movie: '',
        title: '',
        content: '',
        rank: 3,
      },
    }
  },
  methods: {
    ...mapActions(['createReview', 'updateReview']),
  },
  computed: {
    ...mapState({selectedMovie: state => state.movies.selectedMovie}),
    isUpdate () {
      return this.$route.params.isUpdate
    },
  },
  mounted() {
    this.reviewData.movie = this.$route.params.movie_id
    // 수정인 경우, 기본 데이터값들이 나올 수 있도록
    if (this.$route.params.isUpdate) {
      this.reviewData.title = this.$route.params.review.title
      this.reviewData.content = this.$route.params.review.content
      this.reviewData.rank = this.$route.params.review.rank
      this.reviewData['review'] = this.$route.params.review.id
    }
  }
}
</script>

<style scoped>
.upsertreview {
  display: flex;
  flex-direction: column;
  justify-content: center;
  align-items: center;
  min-height: 60vh;

  font-family: 'Noto Sans KR', sans-serif;
  color: aliceblue;
}
/* 리뷰 작성 or 수정 */
.review {
  font-weight: 200;
}

.review-title {
  color: #3396f4;
}

/* select button 시작 */
.box {
  position: relative;
  transform: translate(-50%, -50%);
}

.box select {
  background-color: #0563af;
  color: white;
  padding: 12px;
  width: 250px;
  border: none;
  font-size: 20px;
  box-shadow: 0 5px 25px rgba(0, 0, 0, 0.2);
  -webkit-appearance: button;
  appearance: button;
  outline: none;
  margin: auto;
}

.box::before {
  content: "\f13a";
  font-family: FontAwesome;
  position: absolute;
  top: 0;
  right: 0;
  width: 20%;
  height: 100%;
  text-align: center;
  font-size: 28px;
  line-height: 45px;
  color: rgba(255, 255, 255, 0.5);
  background-color: rgba(255, 255, 255, 0.1);
  pointer-events: none;
}

.box:hover::before {
  color: rgba(255, 255, 255, 0.6);
  background-color: rgba(255, 255, 255, 0.2);
}

.box select option {
  /*padding: 30px;*/
}
/* select button 끝 */

/* input form css 시작 */
.form_group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
  width: 50%;
}

.form_field {
  font-family: inherit;
  width: 100%;
  border: 0;
  border-bottom: 2px solid #9b9b9b;
  outline: 0;
  font-size: 1.3rem;
  color: #fff;
  padding: 7px 0;
  background: transparent;
  transition: border-color 0.2s;
}
.form_field::placeholder {
  color: transparent;
}
.form_field:placeholder-shown ~ .form_label {
  font-size: 1.3rem;
  cursor: text;
  top: 20px;
}

.form_label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: #9b9b9b;
}

.form_field:focus {
  padding-bottom: 6px;
  font-weight: 700;
  border-width: 3px;
  border-image: linear-gradient(to right, #3396f4, #33eef4);
  border-image-slice: 1;
}
.form_field:focus ~ .form_label {
  position: absolute;
  top: 0;
  display: block;
  transition: 0.2s;
  font-size: 1rem;
  color: #3396f4;
  font-weight: 700;
}

/* reset input */
.form_field:required, .form_field:invalid {
  box-shadow: none;
}

/* input form css 끝 */


/*셀렉트박스 */
.optionbox {
    position: absolute;
    /*top: 70%;*/
    right: 12%;
    transform: translate(-50%, -50%)
}

.optionbox select {
    background: #0563af;
    color: #fff;
    padding: 10px;
    width: 200px;
    height: 50px;
    border: none;
    font-size: 20px;
    /*box-shadow: 0 5px 48px rgba(5, 99, 175, 0.89);*/
    -webkit-appearance: button;
    outline: none
}

.optionbox:before {
    content: '\f358';
    font-family: "Font Awesome 5 free";
    position: absolute;
    top: 0;
    right: 0;
    height: 50px;
    width: 50px;
    background: #0563af;
    text-align: center;
    line-height: 50px;
    color: #fff;
    font-size: 30px;
    pointer-events: none
}

.button {
    position: absolute;
    /*top: 70%;*/
    right: 12%;
    transform: translate(-50%, -50%)
}

.button {
    background: #0563af;
    color: #fff;
    padding: 10px;
    width: 200px;
    height: 50px;
    border: none;
    font-size: 20px;
    /*box-shadow: 0 5px 48px rgba(5, 99, 175, 0.89);*/
    -webkit-appearance: button;
    outline: none
}



</style>