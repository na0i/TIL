### 설치사항 



```
npm install -g @vue/cli
```



```
vue create solver-frontend(앱이름)
vue2 선택
cd solver-frontend/
```



```
npm run serve
```



```
vue add router
vue add vuex
npm i axios
```



npm으로 하면 axios를 사용할때마다 import 해주어야 함

router과 vuex는 항상 add로 할 것

lodash도 비슷



- MAIN

  - 공통
    - 현재 인기 질문
    - 이달의 솔버
    - 모임

  - 로그인 한 경우
    - 내가 한 질문
    - 관심 분야 질문

- Navbar

  - 공통
    - 질문/답변 목록 화면
    - 모임 메인 화면
    - 솔버 메인 화면

  - 로그인 한 경우
    - 로그아웃
    - 프로필 페이지
    - 알림_메세지
    - 알림_화상

  - 로그인 안 한 경우
    - 회원가입
    - 로그인

- Footer

- Profile

  - 공통

    - 화상시간 캘린더

    - SOLVE 기록
    - 자기 어필(답변 목록)
    - 팔로잉/팔로워 다이얼로그

  - 노출 프로필

  - 개인 프로필
    - (내가 한) 질문 목록

- Login

- Signup_01

- Signup_02

- Notification_알림  // 두개로 통일한댔나..?

- Notification_보낸 메세지

- Notification_받은 메세지

- Notification_화상

- Notification_알림 전체

- web rtc 화상 화면

  - video 화면
  - 채팅 화면
  - 참관자 화면

- 솔버 메인 화면

- 질문 목록 화면

- 질문 작성 화면

- 질문 상세 화면

  - 화상 요청 다이얼로그

- 모임 메인 화면

- 모임 상세 화면





```bash
solver-frontend
	├── node_modules
	├── public
	└── src
		├── assets
        ├── router
		├── components(view의 alpha, beta 영역을 자유롭게 components로 사용)
		│		├── main
		|		│	├── Navbar.vue
		|		│	└── Footer.vue
        │		├── auth
        │		├── questions
        |		│	├── Answer.vue
        |		│	├── AnswerCreate.vue
        |		│	├── Comments.vue
        |		│	└── CommentsCreate.vue
        │		├── profiles
        │       │	├── ProfileCalendar.vue
        │       │	├── ProfileStatistics.vue
        │       │	├── ProfileHistory.vue
        │       │	└── ProfileMyQuestions.vue
        │		├── groups
        │		│	├── GroupVideo.vue
        │		│	├── GroupQuestion.vue
        │   	│	└── GroupApplicants.vue
        │		├── solvers
        │		├── profiles
        │		├── notifications
        │		├── videos
        │		└── reports
		│
		├── store
        │	├── index.js
        │	└── modules
        │		├── auth.js
        │		├── questions.js
        │		├── groups.js
        │		├── solvers.js
        │		├── profiles.js
        │		├── notifications.js
        │		├── videos.js
        │		└── reports.js
		│
		└── views(router로 움직여야 하는 것)
				├── main
                │   └── Main.vue
        		├── auth
        		│	├── Login.vue
                │   ├── Logout.vue
        		│	├── Signup01.vue
                │	└── Signup02.vue
        		├── questions
                │	├── Questions.vue
                │   ├── QuestionDetail.vue
        		│	└── QuestionCreate.vue
        		├── groups
        		│	├── Groups.vue
                │   ├── GroupDetail.vue
        		│	└── GroupCreate.vue
        		├── solvers
                │	└── Solvers.vue
        		├── profiles
                │	└── Profile.vue
        		├── notifications
                │	├── Notifications.vue
                │	├── NotificationsVideo.vue
                │	├── MotificationsDetail.vue
                │	├── MessageForwarding.vue
                │	└── MessageReceptions.vue
        		├── video
        		└── reports
                	└── Reports.vue
```



drf: axios 쏘는 주소(서버에 뭐 요청하는 주소들)

오른쪽: 화면전환용





부트스트랩 링크로 가져왔고

폰트도 링크로 가져오기
