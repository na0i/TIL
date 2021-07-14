## 1 data, method 작성 방식 변화

기존 코드에서는 props, data, methods가 같은 계층에 존재



Vue3에서는

**props와 setup이 같은 계층에 존재**하고,

**data는 state로, method 들은 각각의 기명함수로 작성**되어 한번에 반환되도록 변화



`예시`

```vue
// Vue 3.x
<script>
export default {
    // props와 setup 같은 계층 존재
    props: {
    	title: String
    },
    setup () {
        // data는 state로 작성
        // state를 그냥 선언 X → vue reactive 사용(반응형, 명시적 선언)
        const state = reactive({
          username: '',
          password: ''
        })
    // methods 각각 작성
    const login = () => {
        // login method
    }
    return { 
        login,
        state
    }
}
</script>
```



## 2 Lifecycle hook 호출 변화

Vue2의 lifecycle hook의 경우에 data, method와 같은 hierachy에서 선언

Vue3에서는 다른 변화들과 같이 **lifecycle hook 또한 setup 내부에서 선언**

그래도, lifecycle hook의 종류는 거의 그대로 유지



`예시`

```vue
<script>
import { onBeforeMount, onMounted, onBeforeUpdate, onUpdated, onBeforeUnmount, onUnmounted, onActivated, onDeactivated, onErrorCaptured } from 'vue'
    
export default {
  setup() {
    onBeforeMount(() => {
      // ... 
    })
    onMounted(() => {
      // ... 
    })
    onBeforeUpdate(() => {
      // ... 
    })
    onUpdated(() => {
      // ... 
    })
    onBeforeUnmount(() => {
      // ... 
    })
    onUnmounted(() => {
      // ... 
    })
    onActivated(() => {
      // ... 
    })
    onDeactivated(() => {
      // ... 
    })
    onErrorCaptured(() => {
      // ... 
    })
  }
}

// state나 method는 return 필요
// lifecycle hook은 return할 필요 없음: 실행이지 반환값이나 할당이 아니므로
</script>
```





## 3 Computed 속성 사용의 변화

computed 속성은 이제 별도 옵션이 아닌,

state 선언문 내에 computed 속성에 대한 선언 구문을 추가하는 방식으로 변경



`예시`

```vue
<script>
// 기존과 다르게 import 해주어야 함
import { reactive, computed } from 'vue'

export default {
  props: {
    title: String
  },
  setup () {
    const state = reactive({
      username: '',
      password: '',
      // computed나 lifecycle hook 등 다양한 옵션들이 함수 형태로 동작하도록
      lowerCaseUsername: computed(() => state.username.toLowerCase())
    })

    // ...
  }
</script>
```





## 4 Composition API

기존(볼륨이 큰 컴포넌트의 경우): 상태 변수(data에 선언된 변수들 등)의 선언, 이 변수들의 computed 메소드 바인딩, methods 함수 선언, lifecycle hook 선언 등이 혼재(유지보수가 굉장히 어려워진다 why? 하나의 feature에 대한 코드가 여기저기로 흩어져서)



Composition API: 가독성이 좋고 코드 안에 논리를 보존하는 방향으로 변화

- Vue의 핵심 기능들을 전부 import하는 대신 직접 선택하여 import

  사용하기 위한 핵심 기능을 import

  ```
  import { reactive, computed } from 'vue'
  ```

- **setup 메소드**: 컴포넌트의 기능들을 **조립(compose)하는 역할**

  lifecycle hook을 걸거나 반응형 데이터 바인딩, computed 사용 등

  마지막에는 꼭 return

  state를 선언 + reactive object로 초기화

  ```
  const state = reactive({
  	username: '',
  	password: '',
  	lowerCaseUsername: computed(() => state.username.toLowerCase())
  })
  ```

- state 호출 시 **this 바인딩 필요 X**

  ```
  const changeName = (name) => {
  	state.username = name
  }
  ```



## 5 props와 this 바인딩의 분리

`기존 예시`: this의 하위 요소로써 prop을 직접 호출

```vue
props: {
	title: String
},

// 생략 //

mounted () {
	console.log('title: ' + this.title)
	// this.title 이 props의 값인지, data인지, method인지
}
```

여기서는 props에서 가져온걸 쉽게 볼 수 있긴 한데

볼륨이 큰 컴포넌트라면 this.title에서 title이 어디서 온 건지 헷갈릴 수 있다.



`예시`

```vue
<script>
// 기존과 다르게 import 해주어야 함
import { reactive, computed } from 'vue'

export default {
	props: {
		title: String
	},
	setup (props) {
	// props를 attribute로 받아왔다.
		onMounted(() => {
            console.log('title: ' + props.title)
            // this 바인딩 아닌 props.title
        })
        // ...
    }
  }
</script>
```

setup은 props를 사용하기 위해서 props를 attribute로 받아야 한다.



## 6 emit과 this 바인딩의 분리

`기존 예시`

```
login () {
	this.$emit('login', {
		username: this.username,
		password: this.password
	})
}
```



`예시`

```
setup (props, { emit }) {
// ...
	const login = () => {
		emit('login', {
			username: state.username,
			password: state.password
		})
	}
// ...
}
```

