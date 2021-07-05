<template>
  <div>
    <div class="upsertreview">

      <div class="container row">
          <div class="col-6 d-flex justify-content-center">
            <img src="@/assets/LOGO_VER2.png" width="50%" style="margin-top: 20vh">
          </div>

          <div class="col-6">
              <div style="margin-top: 20vh">
                <div>
                  <span class="review-title">{{ selectedMovie.title }} </span>
                  <span v-if="isUpdate" class="review">에 대한 리뷰 수정하기</span>
                  <span v-else class="review">에 대한 리뷰 작성하기</span>
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

              <div class="mt-3 underrow">
                <!-- 평점 check box -->
                <span class="col-3 optionbox">
                <span>평점 :  </span>
                <select id="rank" v-model="reviewData.rank">
                    <option value="1">1</option>
                    <option value="2">2</option>
                    <option value="3">3</option>
                    <option value="4">4</option>
                    <option value="5">5</option>
                  </select>
                </span>
                <!-- 평점 check box 끝 -->

                <!-- 제출 button -->
                <div>
                  <span v-if="isUpdate">
                    <button @click="updateReview(reviewData)" class="button"> 수정 완료 </button>
                  </span>
                  <span v-else>
                    <button @click="createReview(reviewData)" class="button"> 작성 완료 </button>
                  </span>
                </div>
                <!-- 제출 button 끝-->
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
  /* justify-content: center; */
  /* align-items: center; */
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
  font-size: 30px;
}

/* input form css 시작 */
.form_group {
  position: relative;
  padding: 15px 0 0;
  margin-top: 10px;
  width: 100%;
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

.underrow {
  display: flex;
  justify-content: space-between;
}

/*셀렉트박스 */
.optionbox {
  font-size: 17px;
}

.optionbox select {
    background: #0563af;
    color: #fff;
    padding: 10px;
    width: 80px;
    height: 50px;
    border: none;
    font-family: 'Noto Sans KR', sans-serif;
    /*box-shadow: 0 5px 48px rgba(5, 99, 175, 0.89);*/
    -webkit-appearance: button;
    outline: none
}

/* .optionbox:before {
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
} */

.button {
    /* position: absolute; */
    /*top: 70%;*/
    /*right: 12%;
    transform: translate(-50%, -50%);*/
}

.button {
    background: #0563af;
    color: #fff;
    width: 200px;
    height: 50px;
    border: none;
    font-size: 17px;
    font-family: 'Noto Sans KR', sans-serif;
    /*box-shadow: 0 5px 48px rgba(5, 99, 175, 0.89);*/
    -webkit-appearance: button;
    outline: none
}



</style>