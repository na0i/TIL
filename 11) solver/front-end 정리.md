### 1. LOGIN

--------------

##### 1) login-dialog

```vue
<template>
  <el-dialog custom-class="login-dialog" title="LOGIN" v-model="state.dialogVisible" @close="handleClose">
    <el-form :model="state.form" :rules="state.rules" ref="loginForm" :label-position="state.form.align">
      <el-form-item prop="userId" label="ID" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.userId" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item prop="password" label="PASSWORD" :label-width="state.formLabelWidth">
        <el-input v-model="state.form.password" autocomplete="off" show-password></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" @click="clickLogin">로그인</el-button>
      </span>
    </template>
  </el-dialog>
</template>
```

`v-model="state.dialogVisible"`: 모달 팝업



```javascript
rules: {
        userId: [
          // trigger: blur → change
          // 1글자씩 변할 때마다
          { required: true, message: 'id는 필수 입력 항목', trigger: 'change' },
          { max: 16, message: '최대 16자까지 입력 가능', trigger: 'change' }
        ],
        password: [
          { required: true, message: 'password는 필수 입력 항목', trigger: 'change' },
          { min: 9, message: '최소 9 글자를 입력', trigger: 'change' },
          { max: 16, message: '최대 16 글자까지 입력 가능', trigger: 'change'},
          {
            pattern: /(?=.*[a-zA-Z])(?=.*[!@#$%^+=-])(?=.*[0-9])/,
            message: 'password는 영문, 숫자, 특수문자가 조합되어야합니다.',
            trigger: 'change'
          }
        ]
      },  
```

rules를 통해 form의 각 필드별 규칙을 정할 수 있었다.

required, 입력 message, max와 min 글자 수, trigger까지 설정할 수 있다.



trigger을 blur에서 change로 바꾸었더니 타이핑 할때마다 검사를 해주었다.





 ```javascript
 const clickLogin = function () {
       // 로그인 클릭 시 validate 체크 후 그 결과 값에 따라, 로그인 API 호출 또는 경고창 표시
       loginForm.value.validate((valid) => {
         // console.log(loginForm.value.validate)
         // [Form]model is required for validate to work!"
         if (valid) {
           store.dispatch('root/requestLogin', { userId: state.form.userId, password: state.form.password })
           .then(function (result) {
             // console.log(result)
             // data: {message: "Success", statusCode: 200, accessToken: "...암튼 담겨왔음 너무길어서 생략"}
               
             store.commit('root/setToken', result.data.accessToken)
             // token에 accessToken 저장
             localStorage.setItem('jwt', result.data.accessToken)
             // store와 localStorage는 별개이므로 localStorage에도 저장해둔다
               
             store.dispatch('root/requestUserInfo', { token: result.data.accessToken })
             // requestUserInfo 라는 action을 token을 담아 dispatch  
               
             .then(function (result) {
               localStorage.setItem('department', result.data.department)
               localStorage.setItem('position', result.data.position)
               localStorage.setItem('userName', result.data.name)
               localStorage.setItem('userId', result.data.userId)
             })
             .catch(function () {
               alert('유저 정보를 불러오는데 실패했습니다.')
             })
             handleClose()
           })
           .catch(function () {
             alert('로그인에 실패했습니다.')
           })
         } else {
           alert('Validate error!')
         }
       });
     }
 ```

로그인 클릭 시 validate 체크 후 그 결과 값에 따라, 로그인 API 호출 또는 경고창을 표시한다.

유효성 검사는 --form.valud.validate로 확인 할 수 있다.

console로 이에 관한 결과를 보면  validate할 때 `[Form]model is required for validate to work!"`가 찍히는 것을 볼 수 있었다.



axios post 요청을 보내면 data에 token값이 담겨오는 것을 확인 할 수 있다.

이를 **store와 localStorage 두곳 모두에 저장**해 두어야 한다.



##### 2) store/root/actions의 requestLogin

```javascript
export function requestLogin ({ state }, payload) {
    
  console.log('requestLogin', state, payload)
  // login-dialog.vue의 79번째 line
  // store.dispatch('root/requestLogin', { userId: state.form.userId, password: state.form.password })에 의해 실행됨
  // console 찍어보면
  // payload: Object 누르면 userId: "user03" password: "user3333!"
    
  const url = '/auth/login'
  let body = payload
  
  // axios에 post 요청을 보낸다.
  return $axios.post(url, body)
}
```

requestLogin은 login-dialog.vue에서 받았던 payload를 담아

axios.post 요청을 보낸다.



##### 3) store/root/actions의 requestUserInfo

```javascript
export function requestUserInfo ({ state }, payload) {
  console.log('requestUserInfo', state, payload)
  // payload에 token 담겨져 왔음
  const url = '/users/me'
  let headers = {
    Authorization : 'Bearer ' + payload.token // 명세서에 명시한대로 hearder에 Bearer+token
  }
  // axios에 get 요청을 보낸다.
  return $axios.get(url, {headers: headers})
}
```

requestUserInfo는 login-dialog.vue 에서 저장한 token을 가지고

headers를 생성해 axios.get 요청을 보낸다.



### 2. SIGN UP

--------

##### 1) signup-dialog

```vue
<template>
  <el-dialog custom-class="signup-dialog" title="SIGNUP" v-model="state.dialogVisible" @close="handleClose">
    <el-form :model="state.form" :rules="state.rules" ref="signupForm" :label-position="state.form.align" @change="checkValidate">
      <el-form-item prop="department" label="DEPARTMENT" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.department" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item prop="position" label="POSITION" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.position" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item prop="name" label="NAME" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.name" autocomplete="off"></el-input>
      </el-form-item>
      <el-form-item prop="userId" label="ID" :label-width="state.formLabelWidth" >
        <el-input v-model="state.form.userId" autocomplete="off"></el-input>
        <el-button type="primary" size="small" @click="checkDuplicate">중복 확인</el-button>
      </el-form-item>
      <el-form-item prop="password" label="PASSWORD1" :label-width="state.formLabelWidth">
        <el-input v-model="state.form.password" autocomplete="off" show-password></el-input>
      </el-form-item>
      <el-form-item prop="passwordConfirmation" label="PASSWORD2" :label-width="state.formLabelWidth">
        <el-input v-model="state.form.passwordConfirmation" autocomplete="off" show-password></el-input>
      </el-form-item>
    </el-form>
    <template #footer>
      <span class="dialog-footer">
        <el-button type="primary" :disabled="state.signupButtonDisabled" @click="clickSignup">가입하기</el-button>
      </span>
    </template>
  </el-dialog>
</template>
```

Login-dialog 코드를 차용해 작성하였기 때문에 로직이 매우 유사하다.



`trigger: 'change'`: 한글자씩 바뀔때마다

```javascript
rules: {
        department: [
          { max: 30, message: '최대 30자까지 입력 가능', trigger: 'change' }
        ],
        position: [
          { max: 30, message: '최대 30자까지 입력 가능', trigger: 'change' }
        ],
        name: [
          { required: true, message: '필수 입력 항목', trigger: 'change' },
          { max: 30, message: '최대 30자까지 입력 가능', trigger: 'change' }
        ],
        userId: [
          { required: true, message: '필수 입력 항목', trigger: 'change' },
          { max: 16, message: '최대 16자까지 입력 가능', trigger: 'change' }
        ],
        password: [
          { required: true, message: '필수 입력 항목', trigger: 'change' },
          { min: 9, message: '최소 9 글자를 입력', trigger: 'change' },
          { max: 16, message: '최대 16 글자까지 입력 가능', trigger: 'change'},
          {
            pattern: /(?=.*[a-zA-Z])(?=.*[!@#$%^+=-])(?=.*[0-9])/,
            message: '비밀번호는 영문, 숫자, 특수문자가 조합되어야합니다.',
            trigger: 'change'
          }
        ],
        passwordConfirmation: [
          { required: true, message: '필수 입력 항목', trigger: 'change' },
          { min: 9, message: '최소 9 글자를 입력', trigger: 'change' },
          { max: 16, message: '최대 16 글자까지 입력 가능', trigger: 'change'},
          {
            pattern: /(?=.*[a-zA-Z])(?=.*[!@#$%^+=-])(?=.*[0-9])/,
            message: '비밀번호는 영문, 숫자, 특수문자가 조합되어야합니다.',
            trigger: 'change'
          },
          { validator: passwordCheck, trigger: 'change' }
        ]
      },
```



validation 검사

```javascript
const clickSignup = function () {
      // 회원가입 클릭 시 validate 체크 후 그 결과 값에 따라, 로그인 API 호출 또는 경고창 표시
      signupForm.value.validate((valid) => {
          
        console.log(signupForm.value.validate)
        // 관리자도구 응답 : [Element Warn][Form]model is required for validate to work!"
          
        if (valid) {
          console.log('submit')
            
      	  // store/root/actions의 requestSignup
          store.dispatch('root/requestSignup', {
            department: state.form.department,
            position: state.form.position,
            name: state.form.name,
            userId: state.form.userId,
            password: state.form.password })
            
          .then(function (result) {
            handleClose()
            alert('SUCCESS')
          })
            
          .catch(function (err) {
            alert('FAIL')
          })
        } else {
          alert('Validate error!')
        }
      });
```

token은 login을 해야 발급되는 것이므로

signup 시에는 해당 사항이 없다.



##### 2) store/root/actions의 requestSignup

```javascript
export function requestSignup ({ state }, payload) {
  console.log('requestSignup', state, payload)
  const url = '/users'
  let body = payload
  return $axios.post(url, body)
}
```

requestSignup은 signup-dialog.vue에서 받았던 payload를 담아

axios.post 요청을 보낸다.



### 3. MAIN HEADER

##### 1) main-header

```javascript
<div class="hide-on-big">
  <div class="menu-icon-wrapper" @click="changeCollapse"><i class="el-icon-menu"></i></div>
  <div class="logo-wrapper" @click="clickLogo"><div class="ic ic-logo"/></div>
  <div class="menu-icon-wrapper"><i class="el-icon-search"></i></div>
  <div class="mobile-sidebar-wrapper" v-if="!state.isCollapse">
    <div class="mobile-sidebar">
      <div class="mobile-sidebar-tool-wrapper">
        <div class="logo-wrapper"><div class="ic ic-logo"/></div>
        <!-- 로그인 되어있는 상태에서는 로그아웃만 보여주기 -->
        <el-button v-if="state.isLoggedin" type="danger" class="mobile-sidebar-btn" @click="clickLogout">로그아웃</el-button>
        <!-- 그 외(로그인 x 상태)에서는 회원가입과 로그인 보여주기 -->
        <div v-else>
          <el-button type="primary" class="mobile-sidebar-btn login-btn" @click="clickLogin">로그인</el-button>
          <el-button class="mobile-sidebar-btn register-btn" @click="clickSignup">회원가입</el-button>
        </div>
      </div>
      <el-menu
        :default-active="String(state.activeIndex)"
        active-text-color="#ffd04b"
        class="el-menu-vertical-demo"
        @select="menuSelect">
        <el-menu-item v-for="(item, index) in state.menuItems" :key="index" :index="index.toString()">
          <i v-if="item.icon" :class="['ic', item.icon]"/>
          <span>{{ item.title }}</span>
        </el-menu-item>
      </el-menu>
    </div>
    <div class="mobile-sidebar-backdrop" @click="changeCollapse"></div>
  </div>
</div>
```

로그인 상태에는 main header에 로그아웃만

비회원 혹은 로그아웃 상태에서는 회원가입과 로그인이 보이도록 구현한다.



```javascript
setup(props, { emit }) {
  const store = useStore()
  const router = useRouter()
  const state = reactive({
    searchValue: null,
    isCollapse: true,
      
    // store.getters의 isLoggedin 불러옴
    isLoggedin: computed(() => store.getters['root/isLoggedin']),
      
    menuItems: computed(() => {
      const MenuItems = store.getters['root/getMenus']
      let keys = Object.keys(MenuItems)
      
      console.log(keys)
      // ["home", "history"] 0: "home" 1: "history" length: 2
        
      let menuArray = []
      for (let i = 0; i < keys.length; ++i) {
        // i=0 or 로그인 상태라면
        // home + history 보여주기
        // 로그아웃 상태일때는 home만 볼 수 있음
        if (i === 0 || state.isLoggedin) {
          let menuObject = {}
          menuObject.icon = MenuItems[keys[i]].icon
          menuObject.title = MenuItems[keys[i]].name
          menuArray.push(menuObject)
        }
      }
        
      return menuArray
    }),
    activeIndex: computed(() => store.getters['root/getActiveMenuIndex'])
  })
```



### 4. LOADING SPINNER

element ui 사이트의 fullscreenLoading을 이용해 구현하였다.



##### 1) conference-detail

```vue
<template>
  <span v-loading.fullscreen.lock="fullscreenLoading">
    {{ $route.params.conferenceId + '번 방 상세 보기 페이지' }}
  </span>
</template>
```



```javascript
    // 처음엔 fullscreenLoading 실행 x
	const fullscreenLoading = ref(false)
    
    // onMounted를 통해 실행된 openFullScreen1 함수에서
    // value를 true로 바꾸어 loading spinner 실행
    // 0.5초 동안 loading spinner 재생 상태
    const openFullScreen1 = () => {
        fullscreenLoading.value = true;
        setTimeout(() => {
          fullscreenLoading.value = false;
        }, 500);
    }


    // 페이지 진입시 불리는 훅
    
    onMounted(() => {
      state.conferenceId = route.params.conferenceId
      store.commit('root/setMenuActiveMenuName', 'home')
        
      openFullScreen1()	// 페이지 진입시 openFullScreen1 함수 실행
        
    })
```

lifecyclehook 중 하나인 onMounted를 이용해

페이지 진입시 loading spinner가 실행되도록 하였다.



현재는 0.5초의 실행기간을 가진 로딩 스피너를 구현하였다.

후에 서버와의 요청과 응답시간에 따른 로딩 스피너 구현이 필요할 것 같다.
