// api/drf.js
export default {
  URL: 'http://localhost:8000/',
  ROUTES: {
    // accounts
    signup: 'rest-auth/signup/',
    login: 'rest-auth/login/',
    logout: 'rest-auth/logout/',
    user: 'rest-auth/user/',
    profile: 'profile/',

    // movies
    initial: 'initial_data/',
    genres: 'genres/',
    search: 'search/',

    // board
    review: 'review/',

  }
}