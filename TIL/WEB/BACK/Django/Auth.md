# Auth
## 개요
Django authentication 과정에 대해 기술한다.

```python
# 로그인 로그아웃
django.contrib.auth.login
django.contrib.auth.logout
# admin.py
django.contrib.auth.admin.UserAdmin
# form
django.contrib.auth.forms.Authentication
# model
django.contrib.auth.models.AbstractUser
```

## Django Authentication System
django에서는 쿠키, 세션에 관한 사전에 준비되어 있는 모듈을 제공한다.

아래와 같은 순서를 따른다.

## Custom User Model
어떤 사용자 정보를 어떻게 저장할 것인지 개발자가 편하게 수정할 수 있도록 별도의 model을 작성하는 것.

**주의!**
```
프로젝트 중간에 `AUTH_USER_MODEL`을 수정할 수 없다.

따라서 프로젝트의 시작과 동시에 custom user model을 만들어 놓고 프로젝트를 진행하는 습관을 들이도록 한다.
```

### 0. 계정 정보를 관리할 accounts 앱 만들기
`python manage.py startapp accounts`

앱을 만들고 settings.py에 등록한다.

### 1. AbstractUser 모듈을 상속하여 별도의 class를 models.py에 저장한다.
계정을 관리할 앱의 models.py에 계정을 관리할 class를 선언한다.

```python
# accounts/models.py
from django.contrib.auth.models import AbstractUser

class User(AbstractUser):
    pass
```

### 2. AUTH_USER_MODEL 수정
settings.py에 AUTH_USER_MODEL 변수를 할당한다.

```python
# project/settings.py
AUTH_USER_MODEL = 'accounts.User'
```

### 3. admin site에 대체한 User 모델 등록
기본 auth.user와 다르게 등록해 줄 필요가 있다.

```python
# accounts/admin.py
from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import User

admin.site.register(User, UserAdmin)
```

## Login & Logout
Login은 session을 만드는 과정이다.

Django에서 다루는 login 관련 내용을 기술한다.

핵심 모듈
```python
# form. 일반적인 form을 사용하듯이 사용하면 된다.
from django.contrib.auth.forms import AuthenticationForm
# auth_login(request, form.get_user())
from django.contrib.auth import login as auth_login
# auth_logout(request)
from django.contrib.auth import logout as auth_logout
```

### 1. login 함수 작성
Create 로직과 유사하게 어떤 method로 요청이 왔는지에 따라서 반환을 다르게한다.

```python
def login(request):
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            auth_login(request, form.get_user())
            return redirect('articles:index')
    else:
        form = AuthenticationForm()
    context = {
        'form' : form,
    }
    return render(request, 'accounts/login.html', context)
```

### 2. logout 함수 작성
logout 함수는 더 간단하다.

request에 session id가 저장되어 있으니 logout에 request만 넘겨주면 된다.

```python
def logout(request):
    auth_logout(request)
    return redirect('articles:index')
```

## Template에서 Authentication data 사용하는 방법
context processor를 통해서 django에서 미리 준비한 user라는 context를 사용한다.

models.py에서 정의한 field를 접근할 수 있다.

기본 값은 아래와 같다.
```
username

password

email

first_name

last_name
```

## etc

### http의 특징

1. 비연결 지향 : 서버는 요청에 대한 응답을 보낸 후 연결을 끊는다.
2. 무상태 : 연결을 끊는 순간 Client와 server 간의 통신이 끝나며 상태 정보가 유지되지 않음.

그럼 로그인, 장바구니 등 요청하는 주체를 서버 측에서 기억하려면 어떻게 해야할까?

서버 측에서 간단한 정보를 전송하여 브라우저가 기억하게 만들고, client가 다음에 요청을 보낼 때 해당 정보를 같이 보내서 같은 주체임을 서버가 알도록 만든다.

이 정보를 쿠키라고 부른다.

### 쿠키
쿠키는 기본적으로 key-value 쌍으로 저장되며, 사용자 인증, 추적, 상태 유지 등에 사용된다.

쿠키에는 도메인, 만료 시간, 경로, 세션 등 다양한 정보가 저장된다.

쿠키는 주로 아래의 기능을 수행한다.

1. 세션 관리 : 로그인, 아이디 자동 완성, 공지 하루 안보기 등...
2. 개인화 : 사용자 선호 설정 (테마, 언어...) 저장
3. 트래킹 : 사용자 행동을 기록 및 분석.

### Session
세션은 서버 측에서 생성하여 클라이언트와 서버 간의 상태를 유지하는데 쓰인다.

쿠키에 세션 데이터를 저장하고 매 요청 시 마다 세션 데이터를 함께 보낸다.

세션은 아래와 같은 순서로 활용된다.

1. 로그인 요청, 인증 성공하면 session 데이터 생성, 저장.
2. 생성된 session 데이터에 인증할 수 있는 session id 발급.
3. session id를 클라이언트에 응답. (데이터는 서버에 저장, 열쇠만 주는 것.)
4. client는 응답 받은 session id를 쿠키에 저장.
5. client가 다시 서버에 접속을 요청하면 요청과 함께 쿠키(session id가 저장된)를 서버에 전달.
6. 쿠키에서 session id를 보고 server는 사용자를 확인.