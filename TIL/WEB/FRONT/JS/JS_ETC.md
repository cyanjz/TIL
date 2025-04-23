# 비동기 함수 `setTimeout`
- 지정된 시간이 지난 후에 실행되는 함수.
- callback 함수를 비동기적으로 실행하므로, 다른 코드의 실행을 방해하지 않는다.
```js
setTimeout(() => {
  console.log('b')
}, 3000)
```