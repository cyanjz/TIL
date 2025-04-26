# JS basic syntax

기본적으로 `<script></script>` tag 내에 작성한다.
<br/>

## 변수
js에서 변수를 선언하는 방식에는 `let`, `const`, `var` 3가지가 존재한다. `var`은 예전 문법이므로 존재는 하지만, `let`, `const`로 작성할 것을 권장한다.

1. block scope는 `{}`로 둘러싸인 영역을 의미한다.
2. 대부분의 경우에 `const` 사용을 권장하고, 재할당이 필요할 때만 `let`을 사용한다.
   1. 사용 의도를 명확하게 할 수 있음.
   2. 버그 예방.
### `let`
- 블록 스코프를 갖는 지역 변수를 선언.
- 재할당 가능.
- 재선언 불가능.
- ES6에서 추가됨.
```js
let number = 10
number = 20 // 재할당, 가능
let number = 30 // 재선언, 불가능
```

### `const`
- 블록 스코프를 갖는 지역 변수를 선언.
- 재할당 및 재선언 불가능.
- ES6에서 추가.
```JS
const number = 10
number = 20 // 재할당, 불가능
const number = 30 // 재선언, 불가능
```