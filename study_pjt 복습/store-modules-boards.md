```javascript
const actions = {
    // 리뷰 생성
    createReview({getters, commit}, reviewData) {
        axios.post(DRF.URL + `${reviewData.movie}/review/`, reviewData, getters.config)
        	.then((res) => {commit('SET_REVIEW', res.data)})
        	.then(() => router.push({name: 'ReviewDetail', params: {movie_id: reviewData.movie, review_id: this.state.boards.selectedReview.id}}))
        	.catch(err => console.log(err))
    },
    
    // 리뷰 불러오기
    fetchReview({commit}, {movie, review}) {
        axios.get(DRF.URL + `${movie}`/review/`${review}`)
    }
}
```

