# Java script basic2

Data type, operators, logic flow control, functions.

## 1. Data types
### Primitive types
- 변수에 값이 직접 저장되는 자료형. (불변, 값이 복사된다.)
#### `Number`
1. 개요
Number type은 정수 및 실수를 나타내는 데이터 타입이다.
```js
const a = 13
const b = -5
const c = 3.14
const d = 2.9e10
const e = Infinity
const f = -Infinity
const g = NaN  // Not a number
```

2. 관련 method 및 `NaN`
- 아래와 같이 잘못된 연산을 수행할 경우에 `NaN`이 할당된다.
```js
const a = '나'/2  // NaN
```
- `isInteger()`
```js
const a = 13
console.log(a.isInteger(()))  // true
```

#### `String`
```js
const a = 'bar'
// 1. toUpperCase
const b = a.toUpperCase()
console.log(a)
console.log(b)

// 2. concat with plus
// * is not supported
const c = a + b
console.log(c)  // barBAR

// 3. template literals (String formatting)
// backticks are used.
// `` also supports multi-line string.
const d = `
안녕하세요.
${a}, ${b}입니다.
`
```

#### `null`, `undefined`
- `null` : 개발자가 값이 없음을 명시.
- `undefined` : 시스템, JS 엔진이 값이 지정되지 않음을 명시.
```js
let a = null
let b  // undefiend
```

#### `Boolean`
- `true`, `false`로 논리적 참과 거짓을 나타내는 자료형.
- python의 `truthy`, `falsy`와 유사하게 자동 형 변환을 제공.

| 타입 (types) | false 로 간주되는 값 | true 로 간주되는 값 |
|--------------|----------------------|---------------------|
| undefined    | 항상 false           | X                   |
| null         | 항상 false           | X                   |
| Number       | 0, -0, NaN           | 나머지              |
| String       | 빈 문자열            | 나머지              |


### Reference type
- 객체의 주소가 저장되는 자료형. (가변, 주소가 복사됨.)
- `Objects` (`Object`, `Array`, `Function`)

## 2. Operators
### arithmetics & logical
```js
// 1. arithmetics
+=
-=
*=
/=
%=
++
--

// 2. logical
>=
>
<
<=
```

### `==` vs. `===`
#### `==` 동등 연산자
- 두 피연산자가 같은 값으로 평가되는지 비교 후 `Boolean`값을 반환.
- 참조형의 경우 같은 객체를 가리키는지 비교.
- 암묵적 타입 변환을 통해 타입을 일치시킨 수 같은 값인지 비교.
```js
console.log(1 == '1')  // true
console.log('hello' == 'hello')  // true
console.log(1 == 1)  // true
console.log(0 == false)  // true
```

#### `===` 일치 연산자
- 두 연산자의 값과 타입이 같거나, 같은 객체를 가리키는 경우 `true`를 반환.
- 엄격한 비교, 암묵적 형변환이 일어나지 않는다.
- 대부분의 경우 일치 연산자 사용이 권장된다.
```js
console.log(1 === '1')  // false
console.log('hello' === 'hello')  // true
console.log(1 === 1)  // true
console.log(0 === false)  // false
```

## 3. Flow control
### `if`
```js
const name = 'customer'

if (name === 'admin') {
    console.log('관리자님, 안녕하세요.')
} else if (name === 'customer') {
    console.log('고객님 환영해요')
} else {
    console.log(`반갑습니다. ${name}님`)
}

// tenary operator
// (condition) ? expression1 : expression2
// expression1 -> when the condition is true
// expression2 -> when the condition is false
const temp = (2 > 4) ? 100 : 1000  // 1000
```

### `while`
```js
while (condition) {
    statements
}
```

### `for`
- `let`을 사용해야함에 유의한다.
- 아래의 두 방법은 매 loop 마다 property가 삭제되고 초기화되므로 `const` 사용을 권장한다.
```js
for (init; condition; change;) {
    statements
}

for (let i = 0; i < 10; i ++) {
    console.log(i)
}
```

### `for in`
- `object`의 property를 순회.
- `iterator` 또한 0, 1, 2의 property를 가진 object로 볼 수 있으므로 `for in` 구문을 사용해도 에러는 발생하지 않으나, index의 순서를 보장하지 않기 때문에 권장하지 않는다.
```js
for (const property in obj) {
    statements
}

const fruits = {'a' : 'apple', 'b' : 'banana'}
for (const property in fruits) {
    console.log(property)  // a, b
    console.log(fruits[property])  // apple, banana
}
```

### `for of`
- `iterator`의 element를 순회.
```js
for (const elem of iter) {
    statements
}

const arr = ['a', 'b', 'c']
for (const elem of arr) {
    console.log(elem)  // a b c
}
```

## 4. Function
### Declaration and Expression
- 참조형 자료형에 속하며, 모든 함수는 `Function` object.
- return이 없을 경우에는 `undefiend`를 반환.
```js
// 1. declaration
//  1) hoisting 가능. -> 비권장.
//  2) 구조, 가독성 측면에서 강점.
function name(p1, p2, p3) {
    statements
    return value
}

// 2. expression - recommended
//  1) hoisting 불가능.
//  2) 익명 함수 사용 가능.
const name = function() {
    statements
    return value
}
```

### Extra
```js
// 1. Default
const func1 = function (p1='asdf') {
    return `Hi ${p1}`
}

// 2. arbitrary (packing)
// python과 유사하게 배열 형태로 전달된다.
// ...p3와 같이 사용.
const func2 = function (p1, p2, ...p3) {
    return [p1, p2, p3]
}

// 3. number of args and params
const func3 = function (p1, p2, p3) {
    return [p1, p2, p3]
}
console.log(func3(1, 2))  // [1, 2, undefiend]
console.log(func3(1, 2, 3, 4))  // [1, 2, 3]
```

### arrow declaration
```js
const arrow = (name) => {return `hello, ${name}`}
```
