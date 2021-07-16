# BACK-END 요구사항

### 1. Database

초기 user 정보를 Table에 Insert하였다.



##### src/main/resources 의 import.sql

![image-20210716035550873](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716035550873.png)



##### MySQL 에서 확인한 user과 conference_category 테이블

password의 12345가 암호화 되어 들어갔음을 확인할 수 있다.

![image-20210716035749466](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716035749466.png)

![image-20210716035836344](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716035836344.png)





### 2. ERD 개요

##### MySQL에서 생성된 ERD

![D](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\D.png)

아쉬운점: 실선이 아닌 점선 형태로 구현되었다.



### 3. JPA

##### Entity

상기 ERD에서 확인 가능



db.entity 파일 마다 아래와 같이 column 지정

![image-20210716040200860](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716040200860.png)



##### Repository

RepositorySupport 대신 Repository를 이용하였다.



예시: UserRepository

![image-20210716040625287](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716040625287.png)





### 4. Swagger

swagger를 이용해 API를 시각화 하고 빠른 테스팅을 진행할 수 있었다.

![image-20210716041329948](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716041329948.png)



##### User 의 회원가입 

![image-20210716042122709](C:\Users\multicampus\Desktop\na0i\S05P1A5074\readme\back-end 정리.assets\image-20210716042122709.png)

swagger를 이용해 요청을 보내고 응답을 받아보았다.

server response와 responces 모두 200 성공이 나와야만 성공이었다.
