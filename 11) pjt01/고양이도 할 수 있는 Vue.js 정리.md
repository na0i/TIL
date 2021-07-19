## 고양이도 할 수 있는 Vue.js



### 머릿말

##### ECMAScript

국제 표준화 단체인 Ecma International에서 책정한 자바스크립트 표준 사양



##### Vue DevTools

크롬 전용 확장 프로그램

Vue.js 개발을 지원해주는 도구



##### 문자열 표기 방법

- 케밥 케이스: my-component
- 카멜 케이스: myComponent
- 파스칼케이스: MyComponent



---------



### CHAPTER 01_Vue.js 프레임워크의 기초

#### 1. Vue.js 개요

##### 프레임워크란

어플리케이션의 뼈대가 되는 기본적인 기능과 규칙 제공

라이브러리는 부품을 조합해 전체를 만들어 나감

프레임워크는 사용할 부품을 우리가 만들어나감



#### 2. Vue.js의 키 컨셉

데이터가 먼저 존재하고 데이터를 기반으로 적절한 DOM을 구축

Data-driven



##### 템플릿

HTML 기반

템플릿과 로직을 연결할 때는 `디렉티브` 라는 기능을 입력해서 사용



##### 데이터 바인딩

데이터와 렌더링을 동기화 하는 구조

자바스크립트 데이터와 이를 사용하는 위치를 연결해 데이터에 변경이 있을 때 자동으로 DOM을 업데이트하는 기능



##### 컴포넌트 지향 화면

컴포넌트: 기능별로 자바스크립트와 템플릿, CSS를 세트로 묶어, 다른 기능과 분리하여 개발 할 수 있도록 함

컴포넌트를 조합하면 페이지를 구조화해서 만들 수 있음



#### 3. 풍부한 리소스 활용하기

`AwesomeVue` 나 `VueCurated` → 범용적인 리소스 많음



`Element`: 웹사이트 전용 UI 컴포넌트 모음

`Onsen UI`: 하이브리드 모바일 애플리케이션 전용 UI 컴포넌트, 모바일 인터페이스 쉽게 구축 가능



#### 5. Vue.js의 기본 기능

디렉티브와 템플릿을 연동하는 형태로 사용



##### 텍스트 바인딩

템플릿에 속성 이름을 작성하면, 해당 위치에 값이 렌더링됨



```html
<p>{{ message }}</p>
```

```javascript
var app = new Vue({
    el: '#app',
    data: {
        message: 'Hello Vue.js'
    }
})
```



##### 반복 렌더링

v-for 디렉티브로 반복 렌더링 가능

```html
<ol>
    <li v-for="item in list">{{ item }}</li>
</ol>
```

```javascript
var app = new Vue({
    el: '#app',
    data: {
        list: ['사과', '바나나', '딸기']
    }
})
```



실제 렌더링 결과

```html
<ol>
    <li>사과</li>
    <li>바나나</li>
    <li>딸기</li>
</ol>
```



##### 이벤트 사용

DOM 이벤트 바인딩(연결)을 할 때는 v-on 디렉티브 사용



##### 입력 양식과 동기화

데이터와 입력 양식의 입력 항목을 바인딩

v-model 디렉티브 사용



```html
<p>{{ message }}</p>
<input v-model="message">
```

```javascript
var app = new Vue({
	el: '#app',
	data: {
		message: '초기 페이지'
	}
})
```



숫자로도 입력값 받기 가능

```html
<input v-model.number="count">
```



##### 조건 분기

v-if 디렉티브를 사용하면 템플릿 기반의 조건 분기 실시 가능



show 속성이 True일 때만 p 요소 렌더링

```html
<p v-if="show">Hello Vue.js</p>
```

```javascript
Var app = new Vue({
    el: '#app',
    data: {
        show: true
    }
})
```



##### 트랜지션과 애니메이션

<transition> 태그를 사용하면, CSS 트랜지션과 애니메이션 손쉽게 적용 가능 

```html
<button v-on:click="show!=show">변경하기</button>
<transition>
	<p v-if="show">Hello Vue.js</p>
</transition>
```

```javascript
Var app = new Vue({
    el: '#app',
    data: {
        show: true
    }
})
```



opacity 0에서 1까지 페이드인&페이드아웃 효과 적용

```css
.v-enter-active, .v-leave-active {
    transition: opacity 1s;
}

.v-enter, .v-leave-to {
    opacity: 0
}
```



#### 6. 옵션의 구성 살펴보기

##### 기본적인 옵션 구성

```vue
var app = new Vue({
	// 마운트 할 요소
	el: '#app',
	
	// 어플리케이션에서 사용할 데이터
	data: {
		message: 'Vue.js'
	},

	// 산출 속성
	computed: {
		computedMessage: function () {
			return this.message + '!'
		}
	},
	
	// 라이프 사이클 훅
	created: function() {
		console.log('created')
	},
	
	// 어플리케이션에서 사용할 메서드
	method: {
		myMethod: function() {
			console.log('method')
		}
	}

})
```



##### 1️⃣ 마운트 할 요소

el에는 어플리케이션 인스턴스를 적용할 요소를 나타냄



##### 2️⃣ data 데이터

객체 또는 배열로 지정하는 것이 일반적



##### 3️⃣ computed 산출 속성

함수로 인해 산출되는 데이터

어떤 처리를 해서 결과를 리턴



##### 4️⃣ 라이프사이클 훅

Vue.js의 기상과 취침까지의 일정한 사이클

Vue.js는 라이프 사이클을 미리 등록해 적절한 시기에 자동으로 호출

이러한 시점을 낚아채서(Hook) 우리가 원하는 처리를 할 수 있게 함



`created`

- 인스턴스 생성, 리액티브 데이터 초기화 된 직후에 호출
- 아직 DOM이 구축되지 않은 상태라 DOM 접근은 불가(html 접근 X)



`mounted`

- DOM 을 만든 직후에 호출
- 하지만, 모든 자식 컴포넌트가 마운트되었다는 것은 보증하지 X



##### 5️⃣ 메서드

코드 관리가 쉽도록 처리를 나누거나, 이벤트 번들러 구현에 사용





#### 정리

- DOM 구조 본체는 자바스크립트 데이터
- new Vue()는 한 개만 만들고, 컴포넌트로 UI를 구축



--------



### CHAPTER 02_Vue.js 데이터 등록과 변경

#### 07. 데이터 바인딩

DOM 변경을 자동화하는 데이터 바인딩을 하려면, 템플릿에서 사용하는 모든 데이터를 리액티브 데이터로 정의해야함



##### 리액티브 데이터란

리액티브 시스템: DOM  변경을 최적화, 데이터 동기화, 변경 감지



##### 리액티브 데이터 정의

컴포넌트의 data 옵션에 문자열 혹은 객체 등의 데이터를 정의하면,

인스턴스 생성 때 모두 리액티브 데이터로 변환됨



```javascript
Var app = new Vue({
    el: '#app',
    data: {
        message: 'Vue.js'	// 이렇게 정의된 message는 변화를 감지할 수 있음
    }
})
```

옵션 외부에 데이터 정의해도

Vue.js 데이터로 등록하면 모두 리액티브 데이터로 변환됨



#### 08. 텍스트와 속성 데이터 바인딩

##### 텍스트와 데이터 바인딩

속성 이름을 이중중괄호로 감싸서 템플릿에 입력( `{{ 이중 중괄호 }}` : Mustache)

텍스트 콘텐츠의 해당 위치에 속성을 바인딩 한다는 의미

한번 화면에 렌더링 된 데이터를 반영하면, DOM이 자동으로 변경됨



##### 객체와 배열 내부의 요소 출력하기

루트에 정의한 속성 뿐만 아니라, `객체 내부의 속성`과 `배열의 요소`도 지정 가능



```javascript
Var app = new Vue({
    el: '#app',
    data: {
        
        // 객체 데이터
        message: {
        	value: 'Hello Vue.js!'
        },
        
        // 배열 데이터
        list: ['사과', '바나나', '딸기'],
        
        // list에서 값을 추출하기 위한 요소
        num: 1
    }
})
```

```html
<p>{{ message.value }}</p>				# Hello Vue.js
<p>{{ message.value.length }}</p>		# 13
<p>{{ list[2] }}</p>					# 딸기
<p>{{ list[num] }}</p>					# 바나나
```



##### 속성 데이터 바인딩 하기



