# Request & response



## 목차

## 개요
Django에서 이뤄지는 request와 response에 대해 기술합니다.

## HTML from & input
기초적인 GET은 html의 form과 input tag를 통해 이뤄진다.

### form
- action : 요청을 보낼 주소
    - 지정하지 않으면 현재 페이지의 URL로 보낸다.
- method : 요청을 보낼 방식
    - 대표적으로 GET과 POST가 있다.

### input
사용자의 데이터를 입력 받을 수 있는 요소.
- id : 다른 요소와 상호작용하기 위한 attribute
    - 아래의 예제에서는 label과 상호작용.
- name : 전송할 매개 변수의 key값.
    - action에 해당하는 url에 `?query=input` 형식으로 전송된다.

```html
<form action="https://search.naver.com/search.naver" method='GET'>
    <label for="message">검색어 : </label>
    <input type="text" name="query" id="message">
    <input type="submit">
</form>
```

## Django
HTML에서 보낸 요청을 Django에서는 views.py를 통해 처리한다.

HTML에서 보낸 요청은 특정 views.py의 함수를 호출한다.

이때 함수가 받는 request에 요청과 관련된 데이터가 포함된다.

위의 예시를 들어 form 과 input tag를 사용해서 매개변수를 받을 경우 `request.GET`에 변수들이 dictionary 형태로 주어진다.

이때 dictionary의 key는 input tag의 name이고, value는 사용자의 입력값이다.

request를 통해 context dictionary를 만들어 render 함수에 전달할 수도 있다.


## ETC
1. 유저 authenticated 여부
`request.user.is_authenticated`