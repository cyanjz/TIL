# Validator
[Validators | Django Document | Django](https://docs.djangoproject.com/en/4.2/ref/validators/#urlvalidator)
## Quick start
validators를 models.field에 validators 인자로 넣어준다.

`models.IntegerField(validators=[validate_even])`

### 사용자 정의 Validator
1. Validator 정의
```python
from django.core.exceptions import ValidationError
from django.utils.translation import gettext_lazy as _


def validate_even(value):
    if value % 2 != 0:
        raise ValidationError(
            _("%(value)s is not an even number"),
            params={"value": value},
        )
```

2. Validator 사용
```python
from django.db import models


class MyModel(models.Model):
    even_field = models.IntegerField(validators=[validate_even])
```

3. forms 
HTML form을 생성하고 유효성 검사를 처리하며, 데이터를 다루는데 사용되는 form class.
```python
from django import forms


class MyForm(forms.Form):
    even_field = forms.IntegerField(validators=[validate_even])
```

### 내장 validator, Built-in

Django에서 기본적으로 제공하는 validator이다.

`RegexValidator`, `EmailValidator`와 같은 일반적인 Validator class를 제공한다.

세부사항은 암기하지 말고, 필요할 때 가져다 쓸 수 있도록 한다.


## 설명
Models.py를 사용하면 database의 구조를 정의할 수 있다. 이때 Validator를 사용하면 database의 무결성을 좀 더 구체적으로 작성할 수 있다.

즉, db의 특정 field의 값 중에서 Validator를 통과하지 못하는 값이 존재하면 `ValidationError`를 발생시킨다.

구체적인 사항은 공식 문서를 참조한다.