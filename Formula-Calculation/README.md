# 2. 수식의 계산

## 1. 중위 표기 -> 후위 및 전위 표기

<img src="https://user-images.githubusercontent.com/41320453/184066955-c22f4dcf-6b4b-4d0d-a658-16b0c0d81bc2.png" width="50%" height="50%">
<br>

### 1. 두 패스가 필요한 방법

<img src="https://user-images.githubusercontent.com/41320453/184067056-bad69ab2-0ef3-4f7a-a189-29c03250272d.png" width="50%" height="50%">

1. 식을 모두 괄호로 묶는다.
2. 이항 연산자들을 모두 그들의 오른쪽(후위 표기) 혹은 왼쪽(전위 표기)에 있는 괄호로 대체시킨다.
3. 모든 괄호를 삭제한다.

- **단점: 비효울 적이다.** (괄호 묶기, 연산자 이동, 총 2단계의 연산이 필요하다.)
<br>

### 2. 스택을 이용한 단일 패스 방법

<img src="https://user-images.githubusercontent.com/41320453/184067076-826f07e6-e8e9-4ed8-9588-8ae6142b56ec.png" width="50%" height="50%">

1. Stack의 top(isp)가 비교하려는 연산자(icp) 보다 크거나 같을 때 스택의 pop 연산을 수행해 준다.
2. 수식에 관호가 존재할 때, 괄호 내 수식은 다른 연산자들에 비해 높은 우선순위를 가진다.
