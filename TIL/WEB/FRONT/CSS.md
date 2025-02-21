# CSS
Cascading Style Sheet. 웹 페이지의 디자인과 레이아웃을 구성하는 언어.
## 1. CSS의 구성.
### Selector (elements to apply css)
기본 구조
```HTML
a {
    color:blue;
}
```
1. Basic selector
    - \* : HTML의 모든 요소를 선택.
    - p (tag selector) : HTML의 특정 태그를 선택.
    - .classname (class selector) : class attribute가 classname인 요소들을 선택. 특정 스타일을 재사용하기 위함.
    - #id_value (id selector) : id attribute가 id인 요소를 선택.
    - a[attr="smthing"] (attribute selector) : attr 속성이 "smthing"인 a 요소를 선택.
      - a[attr] : attr 속성을 가진 a 요소를 선택.
2. Combinators
    - " " : 자손 결합자. 내부의 모든 요소에 적용.
    - \> : 자식 결합자. 내부의 1단계 요소에 적용.
3. 