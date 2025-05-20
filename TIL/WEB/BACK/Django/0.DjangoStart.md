# 0. django 시작
파이썬 가상 환경 설치 및 실행
`python -m venv venv`
`source venv/Scripts/activate`

package 설치
`pip install -r requirements`

프로젝트 만들기
`python manage.py startproject pjt_name .`

앱 만들기 및 등록
`python manage.py startapp app_name`
```python
# pjt_name/settings.py
INSTALLED_APPS = [
    'app_name',
    ...
]
```

# 1. DB 구축
## 1-1. makemigrations
models.py -> models.Model 상속받은 class 선언
class에는 class 변수를 선언하여 field를 정의해주기
```python
class TableName(models.Model):
    col1 = models.CharField(max_length=10)
    col2 = modles.TextField()
    col3 = models.DateTimeField(auto_now_add=True)
    col4 = models.DateTimeField(auto_now=True)
```

makemigrations 수행
`python manage.py makemigrations`

## 1-2. migrate
만들어진 migrations 파일을 바탕으로 실제 db를 구축하는 과정
`python manage.py migrate`


# 2. CRUD 구현
모든 기능을 구현할 때는 url -> view -> template 순서로 작업하기.
