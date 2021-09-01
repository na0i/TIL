### 클래스와 객체2 (4) - singleton 패턴



단 한 개만이 존재하는 객체 - singleton

(ex. 날짜)



`default constructor`를 `private`로 만들어서 `여러개`의 객체들이 `함부로 생성될 수 없도록` 한다.

private -> 외부에서 함부로 호출해서 생성 불가능

public 메서드를 통해 호출 가능

![image-20210901215220960](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901215220960.png)



두 개는 같은 instance를 가리키게 된다.

![image-20210901215309861](C:\Users\multicampus\AppData\Roaming\Typora\typora-user-images\image-20210901215309861.png)