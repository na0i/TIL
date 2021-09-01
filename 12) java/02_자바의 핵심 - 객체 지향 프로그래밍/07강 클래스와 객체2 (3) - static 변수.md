### 클래스와 객체2(3) - static 변수



인스턴스는 각각이 가지고 있는 동적인 heap 메모리를 사용한다

static 변수는 그 인스턴스들이 공유하는 부분

이러한 static 변수가 사용하는 메모리를 `data 영역`, `정적 영역`, `상수 영역` 등이라고 불림



인스턴스의 힙메모리는 new 라고 했을 때 할당됨

static은 다름

전체 프로그래밍이 메모리에 load될 때 할당받음



##### static

![image-20210901165734029](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901165734029.png)

![image-20210901165807846](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901165807846.png)





학생 두명이 있다고 했을때 

한명은 학번이 10001번, 나머지 한명은 10002번이라고 한다.

이때 이 학생들의 학번의 기준 숫자를 어디서 받아와야할까?

했을 때 그게 바로 static 변수(클래스변수라고도 함)



student가 입학할때마다 **자동으로 학번이 올라가게** 해보자

```java
package staticex;

public class Student {
    
    // 학번 기준값을 10000으로 준다.
    static int serialNum = 10000;
    
    int studentID;
    String studentName;
    
    // 학생이 증가한다 = constructor가 호출된다
    public Student() {
        // 호출될 때마다 serialNum 증가시키고 그것을 학번으로 부여해보자
        serialNum ++;
        studentID = serialNum
    }
}
```





![image-20210901175000444](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901175000444.png)

![image-20210901175115812](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901175115812.png)



static 변수를 함부로 건드리게 할 수 없으니까 private으로 막아보자

그러면 외부에서 접근이 불가능하니까 getters를 이용해 만들어보자

(값 변경을 막기 위해 setter는 X)

![image-20210901175422716](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901175422716.png)



외부에서 접근은 이렇게

![image-20210901175527889](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901175527889.png)



2번째 경우에 노란줄(warning) 이 발생한 이유는 무엇일까?

`static 메서드는 클래스 이름으로 참조해서 사용하는 것이 권장된다.`





단, static 메서드 안에

지역변수는 사용가능하지만

멤버변수(인스턴스 변수)는 사용 불가능

![image-20210901175830924](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901175830924.png)



why?

지역변수는 메서드가 끝나면 사라짐

static 메서드는 인스턴스 생성과 관계없이 사용됨

하지만 인스턴스 변수는 new 될때 생성됨

그래서 static 메서드에 인스턴스 변수를 넣게 되면

생성되지도 않은 인스턴스 변수가 사용될 가능성이 있기 때문

![image-20210901180110845](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901180110845.png)





##### 변수의 유효 범위

![image-20210901180134640](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901180134640.png)

static에 너무 큰 메모리를 차지하는 변수를 선언하는 것은 자제하자