# WEB 수업 요점 정리

## 1. 웹

- WHATWG가 W3C와의 기술 표준화 주도권 싸움에서 승리 → WHATWG가 현재 웹 표준
- 표준을 잘 지키는 브라우저 1위: Chrome



## 2. HTML

### 2 - 1) HTML이란?

- HTML = Hyper Text Markup Language
  - Hyper Text: 비선형적 텍스트, HyperLink를 통해 다중으로 연결
  - Markup Language: 태그를 이용해 문서나 데이터의 구조 명시
- 웹 페이지를 작성하기 위한 웹 컨텐츠의 의미와 구조를 정의



### 2 - 2) HTML 기본 구조

- root

  - 문서의 최상위 요소
  - head와 body 부분으로 구분

- head

  - 문서 제목(title)
  - 문자코드(meta charset="UTF-8")
  - CSS 선언
  - 외부 로딩 파일 지정

  

  - 해당 문서 정보를 담고 있음
  - 브라우저에 나타나지 X

- body

  - 브라우저 화면에 나타나는 정보
  - 실제 내용

- HTML 기본구조: DOM 트리

  - Document 객체 모델인
  - 트리 자료구조 형태 → HTML 문서를 읽어 들이고 제어하기 좋은 자료구조

- 요소

  - 태그와 내용으로 구성

    ```html
    <h1>contents</h1>
    
    <h1></h1>: 태그
    contents: 내용
    ```

- 속성

  ```html
  <a href="https://google.com"></a>
  
  href: 속성명
  https://google.com: 속성값
  ```

- 시맨틱태그

  - 의미론적 요소를 담은 태그의 등장
  - non-sementic
    - div
    - span
  - sementic
    - header: 헤더, 머릿말
    - nav: 네비게이션
    - aside: 사이드에 위치, 메인컨텐츠와 관련성이 적음
    - section: 컨텐츠의 그룹
    - article: 독립적으로 구분되는 영역
    - footer: 푸터, 마지막 부분
    - h1, table 등

- 시맨틱 웹: 의미와 관련성을 가지는 거대한 데이터 베이스



### 2 - 3) HTML 문서 구조화

- 그룹 컨텐츠 관련 요소
  - < p > : paragraph, 문단
  - < hr > : 수평 가로선
  - < ol >, < ul > : 리스트
    - ol : ordered list (1, 2, 3)
    - ul : unordered list ( ■, ○, ● )
  - < pre >, < blockquote >
  - < div > : non-sementic
- 텍스트 관련 요소
  - < a > : 하이퍼링크
  - < b >, < strong > : bold
  - < i >, < em > : italic
  - < br >, < img >
    - br : 줄바꿈
    - img : 이미지
  - < span > : non-sementic
- form
  - 서버에서 처리될 데이터를 제공 ex) 검색, 로그인 등
  - input 태그 사용
  - action과 method
  - label : 서식 입력 요소의 캡션