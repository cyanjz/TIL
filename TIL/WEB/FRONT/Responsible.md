# 반응형 웹
반응형 웹은 화면 크기에 따라 웹 페이지를 다르게 구성하는 기술이다.

## 목차

#### I. media query
#### II. flex-box
#### III. bootstrap grid-system

## I. media query
CSS에서 기본적으로 제공하는 반응형 웹 구현 방식이다.

media query는 화면 크기, 장치 유형, 해상도 등에 따라 스타일을 다르게 적용하는 방법이다.

### 1. 기본 형태
```css
@media (조건) {
  /* 적용할 스타일 */
}
```

### 2. 예시
아래 코드는 화면 너비가 측정 px 이하일 때 반응형으로 웹을 구현하는 코드이다.

```css
body {
  background-color: lightblue; /* 기본 배경색 */
}

/* 화면 너비가 600px 이하일 때 적용 */
@media (max-width: 600px) {
  body {
    background-color: pink;
  }
}

```