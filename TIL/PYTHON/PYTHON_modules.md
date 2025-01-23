# Modules
## 개요
- 다른 프로그래머가 이미 작성한 코드를 가져다 써서 효율성을 높이자.
## Modules
- 한 파일로 묶인 변수와 함수의 모음. 특정한 기능을 하는 코드가 작성된 파이썬 파일. (.py)
- 예시 - built-in function
```python
# Python 설치한 곳에 math.py 파일이 존재.
import math
print(math.pi)
print(math.sqrt(4))
```
- from 문을 사용한 가져오기
```python
from math import sqrt
print(sqrt(4))
```
- .연산자 : 점 왼쪽 객체에서 오른쪽의 이름을 찾기.
### 주의 사항
- 서로 다른 모듈이 같은 이름의 함수를 제공할 경우 문제 발생.
- 마지막에 import된 이름으로 대체.
```python
from math import pi, sqrt
from my_math import sqrt
```
- `from module import *`는 권하지 않음.
- 해결하려면 as 문을 추가.
```python
from math import pi, sqrt
from my_math import sqrt as my_sqrt
```
### Style guide
- module 까지만 import 할 것을 권장.
```python
from package1.package2 import module
```
### User Defined modules
- __pycache_\_ : module 실행 시에 생성되는 폴더. 모듈의 실행 속도를 높인다.
- .gitignore에 포함시킬 것.

## Python standard library (PSL)
- 파이썬 언어와 함께 제공되는 다양한 모듈과 패키지의 모음.
- `os, sys, math, random, datetime`

## Pacakge
- 연관된 모듈들을 하나의 디렉토리에 모아 놓은 것.
- 분류 (대 -> 소) : Library -> Package -> Modules
- 모듈들의 이름 공간을 구분하여 충돌 방지.
- 효율적으로 관리, 재사용할 수 있도록 돕는 역할.

## pip 파이썬 패키지 관리자
- 외부 패키지 설치할 때 pip을 사용하여 설치 후에 사용.
- python 외부 패키지들을 설치하도록 도와주는 패키지 관리 시스템.
- PyPI(Python Package Index)에 저장된 외부 패키지들을 설치.
- 설치
```python
pip install SomePackage
pip install SomePackage == version
pip install SomePackage >= version
```
- 삭제 및 목록
```python
# 삭제
pip uninstall SomePackage
# 목록 확인
pip list
```