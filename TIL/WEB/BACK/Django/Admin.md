# Admin
## 개요
Admin 개정은 DB에 직접적인 권한을 가지는 관리자 계정이다.

Django에서는 admin 계정을 기본적으로 관리할 수 있도록 지원한다.

## 개정 생성

```bash
python manage.py createsuperuser
```

위 커맨드를 입력하면 id, email(optional), password 등을 입력하여 관리자 계정을 만들 수 있다.

## 결과 확인
관리자 계정을 만들면 database의 auth_user에 관리자 계정의 정보가 저장된다.

```bash
python manage.py runserver
```

서버를 실행하여 `/admin/`으로 이동하면 관리자 계정으로 로그인할 수 있다.

### db 접근 권한 부여
로그인만으로는 특정 db를 `/admin/`에서 수정할 수 없다.

`app_name/admin.py`에서 모델 클래스를 등록해야 사용할 수 있다.

models.py에서 작성한 class이름인 TableName을 전달하여 접근할 수 있도록 한다.

```python
from django.contrib import admin
from .models import TableName

admin.site.register(TableName)
```