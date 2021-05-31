import Vue from 'vue'
import VueRouter from 'vue-router'

import SignupView from '@/views/accounts/SignupView.vue'
import LoginView from '@/views/accounts/LoginView.vue'
import LogoutView from '@/views/accounts/LogoutView.vue'
import ProfileView from '@/views/accounts/ProfileView.vue'

import MovieIndexView from "@/views/movies/MovieIndexView";
import MovieDetail from "@/components/movies/MovieDetail";
import UpsertReview from "@/components/boards/UpsertReview";
import ReviewDetail from "@/views/board/ReviewDetail";
import SearchResults from "@/components/SearchResults";


Vue.use(VueRouter)

const routes = [
  // accounts
  { path: '/accounts/signup', name: 'Signup', component: SignupView },
  { path: '/accounts/login',  name: 'Login',  component: LoginView },
  { path: '/accounts/logout', name: 'Logout', component: LogoutView },
  { path: '/accounts/profile', name: 'Profile', component: ProfileView },

  // movies
  { path: '/', name: 'MovieIndex', component: MovieIndexView},
  // 영화 상세
  { path: '/:movie_id', name: 'MovieDetail', component: MovieDetail},
  // 영화 검색
  { path: '/search', name: 'SearchResults', component: SearchResults},

  // 리뷰 작성
  { path: '/:movie_id/review/', name: 'UpsertReview', component: UpsertReview},
  { path: '/:movie_id/review/:review_id', name: 'ReviewDetail', component: ReviewDetail},
]


const router = new VueRouter({
  mode: 'history',
  base: process.env.BASE_URL,
  routes
})

export default router
