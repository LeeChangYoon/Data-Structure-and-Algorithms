# 패턴 매칭

## 1. KMP 알고리즘의 개요
![image](https://user-images.githubusercontent.com/41320453/184061653-ba626c88-fb72-4ea0-ab41-a4ae13550bd1.png)
![image](https://user-images.githubusercontent.com/41320453/184061660-5fe90601-405e-49ce-ae23-3934487bd5df.png)

- 패턴에 대한 스트링 탐색은 **접두사**와 **접미사**를 이용한다.
- 패턴 내의 문자들을 알고, 스트링 내 문자와 매치되지 않는 패턴 내 위치를 알아냄으로서 스트링 내에서 후진 없이 패턴 내 특정 위치로 부터 탐색을 재개하는 알고리즘이다.
<br>

- 패턴 실패 함수

![image](https://user-images.githubusercontent.com/41320453/184061744-a437d5eb-bed0-4b22-9d06-dca890f02bf0.png)

- 다음과 같은 함수로 정의된다.
![image](https://user-images.githubusercontent.com/41320453/184062318-359af1f9-c0b5-4777-a8d7-43e78a241413.png)
