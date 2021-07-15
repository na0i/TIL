### STORE

#### STATE

```javascript
export default {
  isDesktopPlatform: IsDesktop,
  activeMenu: 'home',
  menus: menuData,
  authToken: localStorage.getItem('jwt')
}
```

authToken: localStorage에서 jwt 가져오기



#### MUTATIONS

```javascript
// state의 authToken을 변경해주기 위해
export function setToken (state, token) {
	state.authToken = token
}
```



#### ACTIONS

```javascript
// API
import $axios from 'axios'

export function requestLogin ({ state }, payload) {
  console.log('requestLogin', state, payload)
  const url = '/auth/login'
  let body = payload
  return $axios.post(url, body)
}

export function requestSignup ({ state }, payload) {
  console.log('requestSignup', state, payload)
  const url = '/users'
  let body = payload
  return $axios.post(url, body)
}


// 명세서(공용 axios 처리): 토큰이 존재할 경우 {Authorization: Bearer 토큰값} 으로 헤더에 전송
// payload: 
export function requestUserInfo ({ state }, payload) {
  console.log('requestUserInfo', state, payload)
  const url = '/users/me'
  let headers = {
    Authorization : 'Bearer ' + payload.token
  }
  return $axios.get(url, {headers: headers})
}

```



#### GETTERS

```javascript
// 로그인 여부 확인
export function isLoggedin (state) {
  return state.authToken ? true : false
}
```

authToken이 있다면 true / 없다면 false 반환