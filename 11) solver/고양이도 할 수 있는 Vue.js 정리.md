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

```html
<input type="text" v-bind:value="message">
```



`v-bind 장식자`

| 장식자 | 의미                                       |
| ------ | ------------------------------------------ |
| .prop  | 속성 대신에 DOM 속성으로 바인딩            |
| .camel | 케밥 케이스 속성 이름을 카멜 케이스로 변환 |
| .sync  | 양방 바인딩                                |



````html
<div v-bind:text-content.prop="message">
    ...
</div>
````



`데이터 내용 확인`

```html
<pre>{{ $data }}</pre>
```

위와 같이 태그를 작성하면, 현재 데이터 전체의 상태가 어떤지 JSON 형식으로 화면에 출력





##### 메서드 내부에서 데이터 또는 다른 메서드에 접근하기

메서드 내부에서는 this를 붙여야 함

this는 인스턴스를 나타내며

new Vue() 로 생성된 인스턴스, new Vue() 로 생성된 인스턴스의 리턴값을 나타냄

예시) 인스턴스가 컴포넌트라면, this는 컴포넌트 인스턴스 자체를 나타냄





##### this가 무엇을 나타내는가

콜백으로 익명 함수를 사용하거나, 다른 라이브러리와 함께 사용할 경우 this의 내용 변경 가능



[잘못된 예]

```javascript
methods: {
	increment: function(){
		setTimeout(function() { this.count++ }, 100)
	}
}
```

이 경우, 콜백 내부의 this는 window 객체





##### 여러개의 속성 데이터 바인딩

```javascript
Var app = new Vue({
    el: '#app',
    data: {
        item: {
            id: 1,
            src: 'item1.jpg',
            alt: '상품1의 썸네일'
        },
    }
})
```

```
<img v-bind="item">  //한 번에 바인딩 가능
<img v-bind="item" v-bind:id="'thumb-'+item.id">  //특정 요소만 따로 지정도 가능
```





##### SVG 데이터 바인딩하기

SVG: 확장 가능한 벡터 그래픽



원의 반지름 변화시키기

```html
<div id="app">
    <svg xmlns="http://www.w3.org/2000/svg" version="1.1">
    	<circle cx="100" cy="75" v-bind:r="radius" fill="lightpink"/>
    </svg>
    <input type="range" min="0" max="100" v-model="radius">
</div>
```

```javascript
new Vue({
	el: '#app',
	data: {
		radius: 50
	}
})
```





#### 9. 템플릿에서 조건 분기하기

v-if와 v-show: 적용한 요소의 출력 여부를 바꿈, 속성 값이 true 일 때만 요소를 출력



##### v-if와 v-show의 차이와 사용 방법 구분

1. v-if 조건으로 렌더링하기

조건 만족 X인 경우 → DOM 레벨에서 제거, 모든 감시도 제거, 컴포넌트라면 인스턴스 제거, 상태 초기화

디렉티브나 컴포넌트 많이 사용하는 경우

그룹으로 만들어 단일 요소에 사용 가능

v-else-if와 v-else 디렉티브를 조합해 여러개 조건 지정 가능



2. v-show 조건으로 출력하기

조건 만족 X인 경우 → 단순하게 display:none 스타일 적용, 눈에 보이지 않더라도 모든 리액티브 데이터에 대한 내부적 감시

컴포넌트나 디렉티브 없고, 변경 빈도 높을 경우 유리

그룹으로 만들어 단일 요소에 사용 불가능



#### 10. 리스트 데이터 출력/변경 하기

##### 요소 반복해 렌더링하기

```html
<li v-for="각 요소를 할당할 변수 이름" in "반복 대상인 배열 혹은 객체"></li>
```



예시

```html
<div id="app">
    <ul>
        // id와 같은 유니크 키가 있어야 DOM으로 렌더링할 때 최적화가 이루어진다.
        // list라는 이름은 data에서 가져왔지만 item 이라는 이름은 본인이 지정
        <li v-for="item in list" v-bind:key="item.id">
            // item이라는 변수명을 아래와 같이 활용 가능(item 속성에 접근 가능)
            ID.{{ item.id }} {{ item.name }} HP. {{ item.hp }}
        </li>
    </ul>
</div>
```

```javascript
new Vue({
    el: '#app'
    data: {
    	list: [
    		{ id : 1, name: '가', hp: 100},
        	{ id : 2, name: '나', hp: 200},   
    		{ id : 3, name: '다', hp: 500},   
    	]
	}
})
```

list 배열에서 v-for 디렉티브를 사용해 요소를 한 개씩 추출

반복 변수로 item이라는 이름 사용, item 속성에 접근해 이름과 hp 출력





##### 인덱스와 객체 키 사용하기

변수 부분을 괄호로 감싸면 배열의 인덱스를 받을 수 있음

```html
<li v-for="(item, index) in list">...</li>
```



객체의 경우 '<값><키><인덱스>' 순서

```html
<li v-for="(item, key, index) in list">...</li>
```





##### 키의 역할

리스트를 변경할 때 요소의 식별과 효율적인 렌더링 처리를 위해

요소에 유니크한 key 속성을 설정하는 것이 권장됨



why? (item1을 제거했을 경우)

- key가 없는 경우: 요소 전체를 변경해야함
- key가 있는 경우: 삭제된 key의 DOM이 제거될 뿐



id 속성을 key로 데이터 바인딩 하는것이 적합함

같은 요소 내부에서 v-for을 두번 사용하면 key 중복이 일어나 오류 발생





##### 반복 렌더링하며 다양한 조건 적용하기

```html
<li v-for="item in list" v-bind:key="item.id" v-if="item.hp < 300 ">
	ID.{{ item.id }} {{ item.name }} HP. {{ item.hp }}
</li>
```





##### 리스트에 요소 추가하기

```html
<input v-model="name">
<button v-on:click="doAdd">몬스터 추가하기</button>
<ul>
    <li v-for="item in list" v-bind:key="item.id" v-if="item.hp < 300 ">
        ID.{{ item.id }} {{ item.name }} HP. {{ item.hp }}
    </li>
</ul>
```

```javascript
new Vue({
	el: '#app',
    data: {
        name: '카메라',
        list: [
            { id : 1, name: '슬라임', hp: 100},
        	{ id : 2, name: '고블린', hp: 200},   
    		{ id : 3, name: '드래곤', hp: 500},   
        ]
    },
    methods: {
        doAdd: function() {
            var max = this.list.reduce(function(a,b) {
                return a > b.id ? a : b.id 		// a가 b.id보다 크면 a, 작으면 b.id
            }, 0)
            this.list.push({
                id: max + 1,
                name: this.name,
                hp: 500,
            })
        }
    }
})
```

data가 아닌 methods 내부에 있어도 v-model과 연동이 가능(name)





##### 리스트에서 요소 제거하기

배열 메서드인 splice 사용



```html
<ul>
    <li v-for="item in list" v-bind:key="item.id" v-if="item.hp < 300 ">
        ID.{{ item.id }} {{ item.name }} HP. {{ item.hp }}
        <button v-on:click="doRemove(index)">몬스터 제거하기</button>
    </li>
</ul>
```

v-for 요소 안에 button을 만들어 어떤 요소를 삭제할 지 구별할 수 있게 함



```javascript
new Vue({
	el: '#app',
	//..
    methods: {
        doRemove: function(index) {
            // 전달받은 index 위치에서 1개만큼 제거하기
			this.list.splice(index, 1)
        }
    }
})
```



이 외에도

push, pop, shift, unshift, splice, sort, reverse 등 다양한 조작 가능





##### 리스트 요소 변경하기

Vue.js는 인덱스 숫자를 사용한 배열 요소 변경이 불가능

```
 this.list[0] = { id : 1, name: '가', hp: 500 }
```



Vue.set 메서드 사용: `this.$set`을 사용해 변경

```
this.$set('변경할 데이터', 'index or key', '새로운 값')
```

```
this.$set('this.list', '0', '{ id : 1, name: '나', hp: 500 }')
```





##### 속성 추가하기

this.$set은 존재하지 않는 속성을 리액티브 데이터로 추가할 때도 사용

```javascript
new Vue({
	el: '#app',
    data: {
        list: [
            { id : 1, name: '슬라임', hp: 100},
        	{ id : 2, name: '고블린', hp: 200},   
    		{ id : 3, name: '드래곤', hp: 500},   
        ]
    },
    created: function() {
        this.list.forEach(function(item) {
            this.$set(item, 'active', false)
        }, this)
    }
    }
})
```

list 모든 요소에 active라는 속성을 추가





##### 리스트 요소 속성 변경하기

```html
<ul>
    <li v-for="(item, index) in list" v-bind:key="item.id" v-if="item.hp">
        <span v-if="item.hy < 50"> 큰 피해..! </span>
        <button v-on:click="doAttack(index)">공격하기</button>
    </li>
</ul>
```

```javascript
new Vue({
	el: '#app',
	//..
    methods: {
        doAttack: function(index) {
            this.list[index].hp -= 10
        }
    }
})
```





##### 리스트 자체 변경하기

filter 등을 이용해 리스트에 리턴값 다시 할당

```
this.list = this.list.filter(function(el) {
	return el.hp >= 100
})
```





##### 유니크 키가 없는 배열

어떤 조작을 가하기에 적합하지는 않지만 단순 출력 용도면 괜찮음





##### 리터럴에 v-for 적용하기

```html
<span v-for="item in 15">{{ item }}</span>
```

```html
<span v-for="item in [5, 10, 15, 20]"></span>
```





##### 문자열에 v-for 적용하기



```html
<span v-for="item in text">{{ item }}</span>
```

```javascript
new Vue({
    el: '#app',
    data: {
        text: 'Vue'
    }
})
```



실제렌더링

```html
<span>V</span>
<span>u</span>
<span>e</span>
```

이를 활용해 다양한 텍스트 애니메이션을 만들 수 있다.





##### 외부에서 데이터 가져와서 출력하기

데이터가 외부에 있는 경우: JSON 파일 또는 웹 API를 사용해 가져와야함

Ajax 라이브러리 'axios' 사용하기



```javascript
new Vue({
    el: '#app',
    data: {
        // axios로 받아온 데이터를 담은
        // 빈 리스트 미리 준비하기
        list: []
    },
    created: function() {
    	axios.get('list.json')
        .then(function(response){
            this.list = response.data
        }.bind(this))
        .catch(function(e){
            console.error(e)
        })
	}
})
```





#### 11. DOM을 직접 참조하는 $el과 $refs

데이터 바인딩 → DOM에 직접 접근하지 않아도 내용 변경 가능

BUT, 요소의 위치와 높이는 DOM에 직접 접근해야 확인할 수 있음



DOM에 접근할 때는 인스턴스 속성 `$el`과 `$refs`를 사용

DOM을 참조해야 사용할 수 있는 것이므로 **mounted 이후부터 사용 가능**





##### $el의 사용 방법

$el: element의 약어

컴포넌트 템플릿을 감싸고 있는 루트 요소는 $el을 사용해서 DOM을 직접 참조 가능

```javascript
new Vue({
	el: '#app',
    mounted: function(){
        console.log(this.$el)
    }
})
```





##### $ref의 사용 방법

루트 이외의 요소는 특별한 속성 ref와 $refs를 사용해 참조 가능



템플릿에서 대상 요소에  ref 속성을 지정하고 이름을 붙여줌

```html
<div id="app">
    <p ref="hello">Hello</p>
</div>
```

그 후 인스턴스 메서드 내부에서 접근 가능

```javascript
new Vue({
	el: '#app',
    mounted: function(){
        console.log(this.$refs.hello)
    }
})
```





##### $el과 $refs는 일시적인 변경

$el과 $refs는 가상 DOM을 사용하지 X → 렌더링 최적화 X

조작이 발생할 때마다 다시 렌더링 되므로, 자주 변경되는 DOM에는 사용 부적합



```html
<div id="app">
    <button v-on:click="handleClick">Count up</button>
    <button v-on:click="show=!show">표시/비표시</button>
    <span ref="count" v-if="show">0</span>
</div>
```



```javascript
new Vue({
	el: '#app',
    data: {
        show: true
    },
    methods: {
        handleClick: function(){
            var count = this.$refs.count
            if (count) {
                count.innerText = parseInt(count, innerText, 10) + 1
            }
        }
    }
})
```

Count up 버튼을 여러번 누르더라도, v-if로 변경이 일어나면 다시 '0'으로 돌아옴

직접 DOM을 사용해 텍스트를 변경한 것은 가상 DOM에 영향을 끼치지 못함





#### 12. 템플릿 제어 디렉티브

템플릿 또는 컴파일 제어를 위한 디렉티브

| 디렉티브 | 설명                                 |
| -------- | ------------------------------------ |
| v-pre    | 템플릿 컴파일 생략하기               |
| v-once   | 한 번만 바인딩                       |
| v-text   | Mustache 대신 텍스트 콘텐츠로 렌더링 |
| v-html   | html 태그 그대로 렌더링              |
| v-clock  | 인스턴스 준비가 끝나면 제거          |





##### v-pre

자식 컴포넌트를 포함한 내부의 html을 컴파일하지 않고, 정적 콘텐츠로 다룰 때 사용



```html
<a v-bind:href="url" v-pre>
	Hello {{ message }}
</a>
```

Hello {{ message }} 로 그대로 출력





##### v-once

템플릿을 한 번만 컴파일하고 이후에는 정적 콘텐츠로 다룸



```html
<a v-bind:href="url" v-once>
	Hello {{ message }}
</a>
```





##### v-text

요소 내부의 텍스트 콘텐츠가 단일 Mustache만으로 구성되어 있을 경우,

v-text 디렉티브를 사용해 텍스트 콘텐츠 바인딩 가능





##### v-html

html 태그를 직접 출력하고 싶을 때





##### v-cloak

인스턴스 준비가 끝나면 자동으로 제거



```html
<div id="app" v-cloak>
    {{ message }}
</div>
```



```css
[v-cloak] { display: none; }
```

```css
@keyframes cloak-in {
    0% { opacity: 0; }
}

#app {
    animation: cloak-in 1s;
}

#app[v-cloak] {
    opacity: 0;	// 불투명도 100%
}
```

v-cloak 속성이 사라질 때 fade in 효과



---------------

### CHAPTER 03_이벤트와 입력 양식

#### 13. 이벤트 핸들링

`이벤트 핸들러` : 이벤트의 처리 내용

`핸들` : 이벤트 핸들러를 이벤트와 연결하는 것



Vue.js에서는 템플릿 내부에 **v-on** 디렉티브를 이용해 이벤트를 연결

v-on은 생략해서 **@**로 작성할 수 있음



```html
<button v-on:click="이벤트 핸들러">클릭</button>

예시)
<button v-on:click="onClick">클릭</button>
<button @click="onClick">클릭</button>
```

```javascript
new Vue({
    el: '#app',
    methods: {
        onClick: function(){
            alert('클릭')
        }
    }
})
```





##### 인라인 메서드 핸들링

디렉티브 값에 자바스크립트 식을 직접 작성

가독성을 위해 재사용을 거의 하지 않는 짧은 식에만 사용하는 것이 좋다

```html
<button v-on:click="count++">클릭</button>
```



인라인 메서드 핸들러에서는

이벤트 객체 or 사용자 정의 이벤트 매개변수를 `$event`라는 변수 이름으로 사용할 수 있음

(발생한 이벤트의 정보 자체를 가지고 있는 이벤트 객체)

```html
<button v-on:click="handleClick($event, item)">클릭</button>
```





##### 사용할 수 있는 이벤트

예시1) 이미지 로드가 종료될 때 트랜지션 출력

```html
<img src="image.png" v-on:load="show=true" v-bind:class="{hide=!show}">
```

```css
img {
    opacity: 1;
    transition: opacity 1s;
}

img.hide {
    opacity: 0;
}
```

[예시 이해해보기]

처음엔 opacity가 1

v-on:load → 로드가 완료된 후

show=true → show는 true라는 값을 가지고

hide=!show 이므로 → hide는 false값

opacity가 0이 됨



예시2) 동일한 handler 사용

```html
<div v-on:scroll="handler">콘텐츠</div>
<div v-on:mousewheel="handler">콘텐츠</div>
```





##### 입력 양식 입력 추출하기

v-model이 아닌 v-on을 사용해서도 입력 내용 확인, 데이터 할당 가능



```html
<input v-bind:value="message" v-on:input="handleInput"> 
```

```javascript
new Vue({
    el: '#app,'
    data: {
    	message: 'Hello Vue.js'
	},
    methods: {
    	handleInput: function(event){
    		this.message = event.target.value
		},    
    },
})
```

[예시 이해해보기]

원래는 value가 Hello Vue js

input 이벤트 발생하면 message가 event.target의 value(input의 value)로 변경



##### 이벤트 장식자

이벤트 장식자: DOM 이벤트의 기본적인 동작을 변경

| 장식자   | 설명                           |
| -------- | ------------------------------ |
| .stop    | event.stopPropagation()을 호출 |
| .prevent | event.preventDefault()를 호출  |
| .once    | 한 번만 핸들                   |



##### stop: 이벤트 버블링을 막음

(**이벤트 버블링**: 특정 화면 요소에서 이벤트가 발생했을 때 해당 이벤트가 더 상위의 화면 요소들로 전달되어 가는 특성)

86 p 나중에

- 1️⃣2️⃣3️⃣4️⃣5️⃣6️⃣7️⃣8️⃣9️⃣🔟



클릭 이벤트 장식자

| 장식자  | 설명                                       |
| ------- | ------------------------------------------ |
| .left   | 마우스 왼쪽 버튼을 눌렀을 때 핸들러 호출   |
| .right  | 마우스 오른쪽 버튼을 눌렀을 때 핸들러 호출 |
| .middle | 마우스 중간 버튼으로 눌렀을 때 핸들러 호출 |





##### 키 장식자

| 별칭                          | 의미                  |
| ----------------------------- | --------------------- |
| .enter                        | enter 키를 눌렀을 때  |
| .tab                          | tab 키를 눌렀을 때    |
| .delete                       | delete 키를 눌렀을 때 |
| .space                        | space 키를 눌렀을 때  |
| .up / .down / . left / .right | ↑ / ↓  / ← / →        |



##### 시스템 장식자

| 별칭   | 의미                 |
| ------ | -------------------- |
| .ctrl  | ctrl 키를 눌렀을 때  |
| .alt   | alt 키를 눌렀을 때   |
| .shift | shift 키를 눌렀을 때 |





#### 14. 입력 양식 입력 핸들링

`v-model` : 폼 값 또는 선택값을 데이터와 동기화 하는 **양방향 데이터 바인딩** 을 실시할 때 사용



##### v-model 사용방법

```html
<div id="app">
    <input v-model="message">
    <p>{{ message }}</p>
</div>
```

```javascript
new Vue({
    el: '#app',
    data: {
        message: 'Hello'
    },
})
```





##### Vue.js의 양방향 데이터 바인딩

v-model 디렉티브는 두가지 처리를 한번에 작성할 수 있게 함

- 1️⃣ 데이터 바인딩으로 요소의 value 속성 변경
- 2️⃣ 이벤트 핸들링으로 받은 값 데이터에 대입



1️⃣ 데이터 바인딩

데이터 변경을 감지할 때마다 연결된 DOM 요소를 자동으로 변경



    data: {
        message: 'Hello'
    },
데이터

| 속성    | 값     |
| ------- | ------ |
| message | Hello! |

입력 양식에 Hello! 보임



2️⃣ 이벤트 바인딩하기

input 요소처럼 사용자로부터 어떤 입력을 받는 DOM 요소의 경우

입력 이벤트를 트리거로 하여 데이터를 얻을 수 있음



입력양식(Hello) → input 이벤트 발생(Vue.js) → 입력양식(Vue.js == event.target.value)



위와 같은 1️⃣, 2️⃣ 과정을 자동화 해주는 것이 v-model 디렉티브





##### v-model로 받은 데이터의 자료형

일반적인 입력양식은 모든 값을 **문자열 자료형**으로 다룸

여러개를 선택할 수 있는 입력양식의 경우에는 값을 **배열**로 다룸

- **텍스트에리어** : 문자열(단, mustache 사용한 데이터 바인딩 불가능)

- **체크박스**

  - 하나의 요소를 선택할 경우: 기본적으로 Boolean

    ```html
    <label>
    	<input type="checkbox" v-model="val">
        {{ val }}
    </label>
    ```

    ```javascript
    new Vue({
        el: '#app',
        data: {
            val : true
        }
    })
    ```

    

    

    체크 상태에 따라 요소에 값 설정

    true-value와 false-value라는 특별한 속성 사용하기

    ```html
    <input type="checkbox" v-model="val" true-value="yes" false-value="no">
    ```

    

  - 여러개의 요소를 선택: 배열

    각각의 요소에 value 속성을 설정하는 형태로 사용

    ```html
    <label><input type="checkbox" v-model="val" value="A">A</label>
    <label><input type="checkbox" v-model="val" value="B">B</label>
    <label><input type="checkbox" v-model="val" value="C">C</label>
    ```

    ```javascript
    new Vue({
        el: '#app',
        data: {
            val : []
        }
    })
    ```

- **라디오버튼** : 기본적으로 문자열

  (라디오 버튼: 여러 개의 항목 중에서 하나만 선택하도록 하는 동그란 버튼)

  ```html
  <label><input type="checkbox" v-model="val" value="A">A</label>
  <label><input type="checkbox" v-model="val" value="B">B</label>
  <label><input type="checkbox" v-model="val" value="C">C</label>
  ```

  ```javascript
  new Vue({
      el: '#app',
      data: {
          val : ''
      }
  })
  ```

- **선택 박스**

  - 하나의 요소를 선택

    ```html
    <select v-model="val">
        <option disabled="disabled">선택해주세요.</option>
        <option value="a">A</option>
        <option value="b">B</option>
        <option value="c">C</option>
    </select>
    ```

    ```javascript
    new Vue({
        el: '#app',
        data: {
            val : ''
        }
    })
    ```

    

  - 여러 요소를 선택

    ```html
    <select v-model="val" multiple>
        <option value="a">A</option>
        <option value="b">B</option>
        <option value="c">C</option>
    </select>
    ```

    ```javascript
    new Vue({
        el: '#app',
        data: {
            val : []
        }
    })
    ```

- **이미지 파일**: v-model 디렉티브 사용 불가 → change 이벤트 이용해 바인딩

  97 P 참고

- **다른 입력 타입**

  - range

    ```html
    <input type="range" v-model.number="val">{{ val }}
    ```

    ```javascript
    new Vue({
        el: '#app',
        data: {
            val : 50
        }
    })
    ```

    기본적으로 input 요소의 값은 문자열이므로

    숫자 등으로 받고 싶을 때는 `.number` 장식자 등을 활용





##### v-model 디렉티브의 장식자

| 장식자  | 의미                                                         |
| ------- | ------------------------------------------------------------ |
| .lazy   | input 대신 change 이벤트 핸들링하기<br />기본적으로 입력 양식은 입력이 되는 시점에 동기화<br />but, .lazy를 사용하면 change 이벤트가 발생하는 시점에 변경 |
| .number | 값을 숫자로 변환                                             |
| .trim   | 값 양쪽에 있는 쓸데없는 공백 제거<br />줄바꿈 또는 공백 등의 여백을 제거 |





#### 15. 마운트 요소 외의 이벤트 조작

window와 body는 v-on을 사용할 수 x

따라서, window 객체는 addEventListener 메서드를 사용

하지만, v-on과 다르게 없어지는 경우에 핸들러가 자동으로 없어지지 X

즉, 불필요해지는 경우 사전에 훅을 이용해 핸들러를 제거해야함



100P 참고(scroll을 활용한 이벤트)



##### 스무스 스크롤 구현하기

트윈(tween) 계열의 라이브러리 사용해 쉽게 구현 가능



-----------

### CHAPTER 04_데이터 감시하고 가공하기

#### 16. 산출 속성으로 처리 포함한 데이터 만들기

`산출 속성` : 처리를 포함하고 있는 데이터





##### 산출 속성 사용 방법

산출 속성: 임의의 데이터를 리턴하는 함수를 compute 옵션에 정의

```javascript
new Vue({
    el: '#app',
    data: {
        width: 800
    },
    computed: {
        halfWidth: function(){
            return this.width / 2
        }
    }
})
```

```html
<p>
    {{ width }}의 절반은 {{ halfWidth }}입니다.
</p>
```





##### 산출 속성 조합해서 사용하기

산출 속성을 사용해 다른 산출 속성 정의 가능

산출 속성을 여러개로 구분한 뒤 조합해서 사용하면 다양한 활용 가능



```javascript
new Vue({
    el: '#app',
    data: {
        width: 800,
        height: 400,
    },
    computed: {
        halfWidth: function(){
            return this.width / 2
        },
        halfHeight: function(){
            return this.height / 2
        },
        halfPoint: function(){
            return {
                x : this.halfWidth,
                y : this.halfHeight
            }
        }
    }
})
```





##### 게터와 세터

산출 속성은 기본적으로 원래 데이터에 영향을 끼치지 X

따라서, 산출 속성에 값을 대입하면 오류 발생



세터를 활용해 해결 가능

세터: get과 set 속성을 함수로 정의

```javascript
new Vue({
    el: '#app',
    data: {
        width: 800
    },
    computed: {
        halfWidth: 
        	get: function() { return this.width / 2 },
        	set: function(val) { this.width = val * 2}
    }
})
```





##### 산출 속성 캐시 기능

산출 속성

- 리액티브 데이터를 기반으로 결과를 캐시
- 캐시의 트리거가 되는 것은 리액티브 데이터뿐



```html
<ol>
    <li>{{ computedData }}</li>
    <li>{{ computedData }}</li>
</ol>
<ol>
    <li>{{ methodsData }}</li>
    <li>{{ methodsData }}</li>
</ol>
```

```javascript
new Vue({
    el: '#app',
    computed: {
        computedData: function(){ return Math.random() }
    },
    methods: {
        methodsData: function(){ return Math.random() }
    }
})
```

위의 예시에서, 

computed의 computedData는

Math.random()이 리액티브 데이터가 아니므로, 몇번을 실행해도 같은 숫자 리턴됨





##### 리스트 필터링

산출 속성은 원래 데이터에 변경이 있을 때까지 처리를 추가로 실행하지 X

```html
<div id="#app">
    <input v-model.number="budget">원 이하 필터링하기 
    <input v-model.number="limit">개의 결과 필터링하기
    <p>{{ matched.length }}개 중에 {{ limited.length }}개를 출력하고 있습니다.</p>
    <ul>
        <li v-for:"item in limited" v-bind:key="item.id">
        	{{ item.name }} {{ item.price }}원
        </li>
    </ul>
</div>
```

```javascript
new Vue({
    el: '#app',
    data: {
        budget: 300,
        limit: 2,
        list: [
            { id: 1, name: '사과', price: 100 },
            { id: 2, name: '바나나', price: 200 },
            { id: 3, name: '딸기', price: 300 },
            { id: 4, name: '메론', price: 400 },
            { id: 5, name: '오렌지', price: 500 },
        ],
    },
    computed: {
        matched: function() {
            return this.list.filter(function(el) {
                return el.price <= this.budget
            }, this)
        },
        limited: function() {
            return this.matched.slice(0, this.limit)
        }
    }
})
```

112p



※ filter

```
Array.prototype.filter ( callbackfn [ , thisArg ] )


filter 함수의 매개변수는 callbackFunction 과 thisArg 

callbackFunction는 3개의 매개변수를 사용

element : 요소값
index : 요소의 인덱스
array : 사용되는 배열 객체
```





##### 정렬 기능 추가하기

sort는 배열을 직접 조작 → 원래 데이터의 순서를 변화시킴

산출 속성은 데이터에 직접적인 영향을 주는 조작을 하면 안됨



so, 얕은 복사 사용 or Lodash 등의 라이브러리를 사용해야함

```
this.list.sort() → 원래 list 속성도 함께 변경
this.list.slice(0).sort → 요소의 리액티브를 유지하며 배열 복사(0개를 자르니까 전체 복사)
```



```javascript
data: {
    order: false
},
computed: {
    sorted: function() {
        return _.orderBy(this.matched, 'price', this.order ? 'desc' : 'asc')
    },
    limited: function() {
        return this.sorted.slice(0, this.limit)
    }
}
```



※ _.orderBy

```
_.orderBy(a,b,c) a의 b 값을 c 기준으로 정렬

'desc' : 내림차순
'asc' : 오름차순
```







#### 17. 워처로 데이터 감시해서 처리 자동화

일단 프로젝트 급하니까 여기는

나중에 다시 정리



--------------

### CHAPTER 05_컴포넌트로 UI 부품 만들기

#### 21. 컴포넌트란

컴포넌트: 기능을 가진 UI 부품별로 템플릿과 자바스크립트를 세트로 묶어, 다른 UI 부품과 분리해서 개발하거나 관리할 수 있게 하는 방법





#### 22. 컴포넌트 정의 방법

부모가 되는 컴포넌트 템플릿에 사용자 정의 태그를 작성

```html
<div id="app">
    <my-component></my-component>
</div>
```



**data는 함수여야 함**

데이터는 객체를 리턴하는 함수로 정의해야 함

여러개의 컴포넌트 인스턴스들이 같은 객체를 참조해서 상태가 공유되는 것을 회피하기 위해



**루트 요소는 하나여야 함**



##### 컴포넌트 인스턴스

```html
<div id="app">
    <my-component></my-component>
    <my-component></my-component>
</div>
```

같은 컴포넌트를 여러번 사용할 경우, my-component를 기반으로 만들어진

완전히 다른 인스턴스로 취급됨





#### 23. 컴포넌트끼리의 통신

컴포넌트 인스턴스는 각각 스코프를 가지고 있음



스코프

- 영향을 미칠 수 있는 범위
- 간단하게 정의한 데이터, 메서드, 템플릿
- 스코프 내부의 데이터와 메서드는 this를 사용해 접근 가능
- 실수로 다른 기능에 영향을 미치지 않게 하기 위한 것



스코프 덕분에 다른 컴포넌트에 있는 데이터와 메서드에 직접 접근할 수 X

so, 컴포넌트 끼리 데이터를 공유하거나 연동하기 위해서는 

1️⃣ props를 이용해 부모 자식간의 통신

2️⃣ 이벤트 버스를 사용해 통신

3️⃣ Vuex 사용한 상태관리





##### 부모 자식 컴포넌트

템플릿에서 다른 컴포넌트를 사용하면 부모자식 관계가 만들어짐

이렇게 네스트된 컴포넌트는 DOM처럼 트리 구조를 갖게 됨



##### 부모에서 자식으로

부모: val은 사용해도 괜찮아

```html
<comp-child v-bind:val="message" class="item"></comp-child>
```



자식: val을 사용할게

```
props: ['val']
```

template에 val 사용가능





##### 컴포넌트를 리스트 렌더링하기

부모

```html
<ul>
    <comp-child v-for="item in list"
    	v-bind:key="item.id"
        v-bind:name="item.name"
        v-bind:hp="item.hp">
    </comp-child>
</ul>
```



자식

```html
<li>{{ name }} {{ hp }}</li>

props: ['name', 'hp']
```





##### props로 전달받은 데이터는 마음대로 변경하면 안됨

props는 리액티브 상태이므로 부모쪽에서 데이터를 변경하면 자식 쪽의 상태도 변경

but, props 속성은 부모에서 빌린것이므로

자식 컴포넌트에서 값을 마음대로 변경하면 X





##### props로 받을 자료형 지정하기

지정한 자료형 이외의 값이 들어올 경우,

경고도 출력되므로 문제가 발생했을 경우 쉽게 찾을 수 있다.



```javascript
Vue.component('example', {
    props: {
	val: String,
    // 기본적 자료형 확인
	propA: Number,
    
    // 여러개 자료형 지정가능
	propB: [String, Number],
        
    // 필수 문자열    
	propC: {
		type: String,
		required: true
	},
    
    // 디폴트 값
	propD: {
		type: Number,
		default: 100
	},
        
    // 객체와 배열의디폴트 값
	propE: {
		type: Object,
		default: function(){
			return { message: 'hello '}
		}
	},
        
    // 사용자 정의 유효성 검사 함수
    propF: {
        validator: function(value) {
            return value > 10
        }
    }
}
})
```





##### 자식에서 부모로

자식 컴포넌트가 가진 데이터를 부모 컴포넌트에 전달하고 싶을 때는

사용자 정의 이벤트와 `$emit` 이라는 인스턴스 메서드를 사용



**자식 이벤트를 부모에서 잡기**

부모에서 자식 사용자 정의 태그를 작성할 때 v-on(@)으로 이벤트를 핸들

자식은 적당한 시점에서 $emit을 사용해 이벤트를 실행



자식

```html
<button v-on:click="handleClick">
    이벤트 호출하기
</button>
```

```javascript
methods: {
    handleClick: function() {
        this.$emit('child-event')
    }
}
```



부모

```html
<comp-child v-on:child-event="parentMethods"></comp-child>
```

```javascript
methods: {
    parentMethod: function() {
        alert('이벤트 받음!')
    }
}
```





##### 부모 자식 컴포넌트가 아닌 경우(이벤트 버스)

부모 자식 컴포넌트가 아닌 컴포넌트들끼리 데이터를 전달할 경우

Vue 인스턴스의 이벤트 버스라는 기능을 사용

157P





##### 자식 컴포넌트를 참조하는 $refs

`ref`: 경우에 따라서 부모에서 자식의 메서드 혹은 이벤트를 호출하고 싶은 경우도 있음



부모

```html
<comp-child ref="child"></comp-child>
```

```javascript
this.$refs.child.$emit('open')
```



자식

```
created: function() {
	this.$on('open', function() {
		...
	})
}
```





##### 컴포넌트 속성의 스코프

자식 컴포넌트에서 전달된 매개변수는 $event로 접근 가능



```html
<comp-child v-on:childs-events="parentsMethod($event, parentsData)"></comp-child>
```

