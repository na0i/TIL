// api/drf.js
export default {
  URL: 'http://localhost:8000/',
  ROUTES: {
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    logout: 'rest-auth/logout/',
    user: 'rest-auth/user/',
    profile: 'profile/',
    review: 'review/',
    // articles: 'board/articles/',
    // article: `board/articles/`
  }
}