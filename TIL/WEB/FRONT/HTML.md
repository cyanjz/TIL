# HTML
## 1. HTML tags
- <>, </> : 여는 태그, 닫는 태그.
- 닫는 태그를 작성하지 않는 경우
  - Content를 작성하지 않는 경우에는 닫는 태그를 생략한다.
  - `<meta charset=”utf-8”>`

## 2. HTML attribute
- 사용자가 원하는 기준에 부합하도록 할당하는 속성.
  - CSS에서 스타일을 지정할 때 참조하는 용도로 사용될 수 있다.
- 작성 스타일
  - 여는 tag에 작성한다.
  - 여러 attribute를 작성할 경우에는 공백을 기준으로 나누어 지정할 수 있다.
- 예시
  - `<p class=”editor-note”>My cat is very grumpy</p>`

## 3. HTML elements
- HTML을 구성하는 요소. 2개 혹은 1개의 tag로 구성된다.
- 구조를 지정하는 요소들 : html (parent) > head, body (children)
- `<!DOCTYPE html>`, `<html>` : 문서의 시작과 끝 그리고 문서 타입을 명시하는 요소.
    ```HTML
    <!-- Document가 html 파일임을 명시. -->
    <!DOCTYPE html> 
    <!-- html 파일의 시작과 끝을 명시. 내부에 head, body를 작성. -->
    <html></html>
    ```
- `<head>` : 문서와 관련된 메타데이터를 보관하는 요소
    ```HTML
    <head>
        <title></title>
        <style></style>
    </head>
    ```
  - title : 문서의 제목. 즐겨찾기, 탭 이름에서 표시되는 명칭.
  - style : CSS internal style sheet. CSS style을 지정하는 요소.
- `<body>` : 문서 내용을 포함하는 요소.
    ```HTML
    <h1></h1>
    ...
    <h6></h6>
    <p></p>
    <a href="url"></a>
    <img src="" alt="">
    <em></em>
    <strong></strong>
    <ol></ol>
    <ul></ul>
    <li></li>
    ```
#### **HTML의 요소에는 강제적인 규칙이 정해져 있지 않지만, 의미적으로 정해진 규칙이 있음.**
  - `<h1></h1>`의 경우 한번만 작성해야 한다는 규칙은 없지만, '웹페이지의 최상위 제목'이라는 점에서 한번만 사용하는 것이 좋다.


