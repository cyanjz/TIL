# PEP8-convention
이 문서에서는 PYTHON의 Style 규칙인 PEP8에 대해 기술합니다.
## 개요
PEP8은 PYTHON의 코드 작성 일관성을 유지하고 가독성을 높이기 위해 고안되었음.
## 핵심 영역
1. 직관적인 이름을 지을 것. 즉, 변수의 이름만 보고 어떠한 역할을 하는지 알 수 있도록.
2. 들여쓰기는 4칸
3. 한 줄 길이는 79자, 넘어가면 줄바꿈 수행
4. 함수, 변수, 속성은 snake_case로 작성
5. 함수 정의, 클래스 정의등의 블록 사이에는 빈 줄을 추가.
6. 변수명 규칙
   1. 영문 알파벳, _, 숫자로 구성
   2. 숫자 시작 불가능
   3. 대소문자 구분
   4. 예약어 금지

|예약어 목록|         |         |        |
|---------|---------|---------|--------|
| False   | def     | if      | raise  |
| None    | del     | import  | return |
| True    | elif    | in      | try    |
| and     | else    | is      | while  |
| as      | except  | lambda  | with   |
| assert  | finally | nonlocal| yield  |
| break   | for     | not     | class  |
| continue| global  | pass    | form   |
| or      |         |         |        |

## Collections
### Commons
#### Trailing comma
- 줄을 바꿔가면서 collection 선언시에는 마지막 요소 뒤에 comma를 붙인다.
- 한줄로 쓸 때는 사용하지 않는다.
```python
a = [
   1,
   2,
   3,
]
```