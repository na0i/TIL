# CSS 수업 요점 정리

## 1. CSS란?

- 스타일, 레이아웃 등을 통해 html을 표시하는 방법을 지정하는 언어

- CSS 구문

  ```html
  h1 {
  color: blue;
  font-size: 15px;
  }
  
  h1: 선택자(selector)
  'color: blue;', 'font-sizw:15px;': 선언
  color, font-size: 속성(property)
  blue, 15px: 값(value)
  ```

- CSS 정의 방법

  - 인라인: 해당 태그에 직접 style 속성 활용
  - 내부 참조: 한 파일 내, head 태그에 style 지정
  - 외부 참조: 분리된 CSS의 head 내 link를 통해 불러오기



## 2. CSS selector

### 2 - 1) 선택자

- html 페이지 안의 특정 element들을 선택해 선언 블록의 내용을 적용시킴

- 전체 선택자

  - html 페이지 내부 모든 태그 선택
  - *를 사용하여 나타냄

  ```html
  * {
  	margin: 0 auto;
  }
  ```

- 태그 선택자

  - 태그명이 선택자와 같은 태그들에 적용

  - 태그의 이름을 사용해서 나타냄

  ```html
  p {
  	color: red;
  }
  ```

- 클래스 선택자

  - 클래스 이름과 같은 태그들에 적용

  - '.클래스 이름' 을 사용하여 나타냄

  ```html
  .ssafy {
  	width: 100px
  }
  ```

- ID 선택자

  - ID가 ID 이름과 같은 태그에 적용

  - #아이디 이름을 사용해 나타냄



### 2 - 2) CSS 적용 우선순위

- !important > 인라인선택자 > id 선택자 >  class 선택자 >  요소 선택자 > 소스 순서



### 2 - 3) CSS 상속

- CSS는 상속을 통해 부모요소의 속성을 자식에게 상속
- 상속되는 것
  - font, fontcolor, text-align, opacity, visibility 등
- 상속되지 않는 것: box-model 관련, position 관련 요소
  - width, height, margin, padding, border, box-sizing, display, position, top/right/bottom/left 등



### 2 - 4) CSS 크기 단위

- 크기 단위
  - px(픽셀), %, em, rem, vw, vh, vmin, vmax 등
  - em: 상대적인 사이즈
  - rem: 최상위 요소(html) 사이즈 기준 배수 단위



## 3. BOX-MODEL

### 3 - 1) Box-model

- Box model 구성

  - margin

    - 테두리 바깥 외부 여백
    - 배경색 지정 불가능

    ```html
    # margin 일반
    .margin{
    	margin-top: 10px;
    	margin-right: 20px;
    	margin-bottom: 30px:
    	margin-left: 40px;
    }
    
    → top, right, bottom, left
    ```

    ```
    # margin shorthand
    상하좌우 10px
    .margin-1{
    	margin: 10px;
    }
    
    상하+좌우
    .margin-2{
    	margin: 10px 20px;
    }
    
    상+좌우+하(3개=위>중간>아래로 기억하기)
    .margin-3{
    	margin: 10px 20px 30px;
    }
    
    상+우+하+좌(4개=시계방향)
    .margin-4{
    	margin: 10px 20px 30px 40px;
    }
    ```

    

  - border

    - 테두리

    ```html
    # border 일반
    .border {
    	border-width: 2px;
    	border-style: dashed;
    	border-color: black;
    }
    
    → width, style, color
    ```

    ```html
    # border shorthand
    
    .border{
    	border: 2px dashed black;
    }
    ```

    

  - padding

    - 테두리 안쪽 내부 여백

    - 이미지는 padding까지 적용

  - content
    - 요소의 실제 내용



### 3 - 2) Box-size

- width 100px, padding 20px, border 1px일 경우 boxsize는 142px가 되어버림
- box-sizing은 padding을 제외한 순수 content 영역만을 box로 지정하기 때문
- border-box로 설정하기



## 4. CSS Display

### 4 - 1) display

- block
  - 줄바꿈이 일어남
  - 가로폭: 화면 크기 전체
  - 블록 레벨 요소 안에 인라인 레벨 요소 들어갈 수 있음
- inline
  - 줄바꿈이 일어나지 않음
  - 가로폭: content의 너비
  - width, height, margin-top, margin-bottom 지정 X
  - 상하여백은 line-height로
- inline-block
  - block과 inline 요소의 특징 모두
  - inline- 한 줄 에 표시 가능
  - block- width, height, margin 속성 지정 가능
- none
  - 해당 요소 화면에 표시 X, 공간 X
  - visibility: hidden은 표시 X, 공간 O



## 5. CSS position

### 5 - 1) 요소 배치 방법

- static: 디폴트값(좌측 상단)
- relative
  - static 위치를 기준으로 이동
  - 이동할 때 원래 있어야 할 자리를 비워주지 않고 움직임
- absolute
  - 가까이 있는 부모/조상 요소를 기준으로 이동
  - 이동할 때 자리를 비워줌
- fixed
  - 브라우저를 기준으로 이동
  - 스크롤 관계 X

