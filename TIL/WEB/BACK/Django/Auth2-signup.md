# Auth2-signup
## I. 회원 가입 및 수정
### 1. 필요한 폼 정의
`django.contrib.auth.forms.UserCreationForm` : 회원 가입

`django.contrib.auth.forms.UserChangeForm` : 회원 정보 수정

`django.contrib.auth.get_user_model` : 현재 유저 모델을 반환하는 함수. 유지 보수를 위해 사용할 것을 강력히 권고.

두 Model Class를 상속하여 Custom model form을 정의해야한다.

왜냐하면 UserCreationForm과 UserChangeForm은 둘 다 auth.user를 사용해서 업데이트를 수행하려 하기 때문에 재정의된 User model, accounts.User를 바탕으로 DB 조작을 수행하지 않기 때문이다.

```python
from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from django.contrib.auth import get_user_model
from .models import User


class CustomCreationForm(UserCreationForm):
    class Meta(UserCreationForm.Meta):
        model = get_user_model()
        fields = (...)


class CustomChangeForm(UserChageForm):
    class Meta(UserChageForm.Meta):
        model = get_user_model()
        fields = (...)
```

### 2. views.py 작성

1. 생성 로직

```python
...
from .forms import CustomCreationForm, CustomChangeForm


def signup(request):
    # POST 요청일 경우
    if request.method == 'POST':
        # POST의 정보를 바탕으로 form 인스턴스 만들기
        form = CustomCreationForm(request.POST)
        # form이 유효성 검사를 통과한 경우
        if form.is_valid():
            # form을 저장
            form.save()
            # 메인 페이지로 redirect
            return redirect('articles:index')
    # 이외의 요청일 경우
    else:
        # form 생성
        form = CustomCreationForm()
    # POST 요청이 유효성 검사를 통과하지 못했거나 get method로 요청이 온 경우
    context = {
        'form' : form,
    }
    # 로그인 페이지 render
    return render(request, 'accounts/login.html', context)

```


2. 업데이트 로직

```python
def update(request):
    if request.method == 'POST':
        form = CustomChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = CustomChangeForm(instance=request.user)
    context = {
        'form' : form,
    }
    return render(request, 'accounts/update.html', context)
```

업데이트 로직을 작성하여도 비밀번호는 바꿀 수 없다. django에서는 CustomChangeForm rendering을 수행할 때, 비밀번호를 변경할 수 있는 a tag도 같이 제공한다. 해당 a tag의 주소는 `<int:user_pk>/password`의 형태로 주어진다. 따라서 별도의 url 변경 없이 작업할 때는 해당 url로 pjt에 요청이 들어왔을 때, view 함수가 동작하도록 작성한다.

## II. 회원 탈퇴
request 객체의 user를 삭제하면 된다.

```python
def delete(request):
    request.user.delete()
    return redirect('articles:index')
```

## III. 비밀번호 업데이트
1. PasswordChangeForm
`django.contrib.auth.forms.PasswordChangeForm` : 비밀번호를 변경하는 django 제공 form.

첫 인자로 `user` 객체를 받아야한다.

비밀번호는 UserChangeForm을 통해서 수행할 수 없다.

2. 왜 Form을 상속 받았는가

이는 비밀번호가 개념적으로 DB에 바로 업데이트되는 것이 아니라 암호화를 통해 DB에 저장되기 때문에 ModelForm과 구분지어서 Form으로 django에서 상속했기 때문이다.


3. update_session_auth_hash
인자 : request, user

비밀 번호 변경 이후에도 session을 유지하도록 해주는 내장 함수.

```python
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash


def chage_password(request, user_pk):
    if request.method == 'POST':
        form = PassWordChangeForm(request.user, request.POST)
        if form.is_valid():
            user = form.save()
            update_session_auth_hash(request, user)
            return redirect('articles:index')
    else:
        form = PassWordChangeForm(request.user)
    context = {
        'form' : form,
    }
    return render(request, 'change-password', context)
```

# 기타
authenticated user에 대해서만 어떤 작업을 수행하려면 어떻게 해야할까?

1. request.user.is_authenticated
is_authenticated를 통해 사용자가 로그인 되어 있는지를 확인할 수 있다.

dtl 문법에서 해당 요소를 사용하면 특정 요소들을 로그인 여부에 따라서 관리할 수 있다.

또한, view 함수 내에서도 `request.user.is_authenticated`를 사용할 수 있다. 즉, view 함수 내에서도 사용자가 인증된 사용자인지 확인해서 다르게 동작하도록 로직을 구성할 수 있다.

2. @login_required
```python
from django.contrib.auth.decorators import login_required
```

해당 decorator를 view 함수에 붙이게되면 authenticated되지 않은 요청에 대해서는 `/accounts/login/` 주소로 redirect 시킨다. accounts로 앱 이름을 작성하면 가지는 편리성이 여기 있다!