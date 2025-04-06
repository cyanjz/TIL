# Template system
Django의 Template 관련 내용을 다룹니다.

## 목차

#### I. 개요
#### II. DTL
#### III. Template 상속
#### IV. Comments

## I. 개요
Django의 HTML은 일반적인 HTML 문서의 기능을 넘어서 일부 프로그래밍 언어적 기능을 제공한다.

## II. DTL
HTML에서 변수 및 루프, 조건문과 같이 일부 프로그래밍적 기능을 제공하는 문법.

```
tag : {% tag_name %} {% endtag_name %} 또는 {% tag_name %}
variables : {{variable_name}}
filters : {var|filter}, {var|filter1|filter2}, {var|filter:arg}
```

### i. 변수

#### 1. views.py
먼저 특정 template에 사용할 변수를 views.py를 통해 전달해줘야 한다.

이는 render의 세번째 인자인 context에 dictionary 타입으로 전달 해줄 수 있다.

```python
def test(request):
    context = {
        'a' : a,
    }
    return redner(request, '/taget_folder/test.html', context)
```

#### 2. Template
이제 특정 Template에서 context에 포함된 변수에 접근할 수 있다.

다음과 같은 tag를 사용한다.

`{{ a }}`

- a는 context의 key값이다.
- views에서 전달한 dictionary의 key를 통해서 해당하는 value에 접근할 수 있다.



### ii. tags
tag를 사용하면 프로그래밍 언어의 기능을 html 상에서 일부 구현할 수 있다.

내장 태그 및 필터는 다음을 확인한다.

`https://docs.djangoproject.com/en/5.1/ref/templates/builtins/`

#### 양식과 기능.
tag는 다음과 같은 기능을 수행할 수 있다.
- 논리 제어 : 반복과 조건문 등의 수행
- template 상속 : template의 상속을 수행
- 그외.

기본적으로 아래와 같은 구조를 가진다.

단, 종료 태그가 없는 경우도 존재한다.
```
{% tag %}
{% endtag %}
```


### iii. filters
필터는 변수를 수정할 때 사용된다.

기본적인 구조는 아래와 같다.
```
{{variable|filter}}
```

Chained 구조로 작성할 수도 있다.
```
{{variable|filter1|filter2}}
```

인자를 받는 경우도 있다.
```
{{variable|turncatewords:30}}
```

## III. template 상속
template의 공통된 부분이 있을 경우에는 해당 부분을 중복해서 작성하는 것이 아니라, 상속을 받아서 사용할 수 있다.

대표적으로 bootstrap의 CDN을 모든 template에 작성하는 것은 매우 시간 소모가 크고 html이 복잡해진다.

따라서 bootstrap을 비롯한 기본적인 틀을 정의한 html을 만들고, 다른 html들은 해당 html을 바탕으로 문서를 작성할 수 있도록 한다.

이는 `block` tag와 `extends` tag를 통해서 이뤄진다.

크게 두가지 작업을 해줘야 한다.

```
1. base html의 어느 부분에 다른 html의 요소가 들어가야 하는가.
2. 다른 html은 어떤 base html을 상속 받아야 하는가.
```

### 1. base.html
기본이 될 sekelton html 파일에 어떤 부분에 작성할 수 있는지 명시한다.

block tag를 이용하며 다음과 같은 양식을 따른다. 여기서 작성한 block tag의 이름을 child.html에서 사용한다.

```
{% block block_name %}{% endblock block_name %}
```

예시 코드는 아래와 같다.

style tag를 작성할 수 있고, body의 일부를 작성할 수 있다.

```HTML
<!doctype html>
<html lang="en">
  <head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <title>Bootstrap demo</title>
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-QWTKZyjpPEjISv5WaRU9OFeRpok6YctnYmDr5pNlyT2bRjXh0JMhjY6hW+ALEwIH" crossorigin="anonymous">
    <style>
        {% block style %}{% endblock style %}
    </style>
</head>
  <body>
    {% block content %}{% endblock content %}
    <script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" integrity="sha384-YvpcrYf0tY3lHB60NNkmXc5s9fDVZLESaAA55NDzOxhy9GkcIdslK1eN7N6jIeHz" crossorigin="anonymous"></script>
  </body>
</html>
```

### 2. child.html
먼저, 상속 받는 html은 먼저 어떤 html을 상속 받는지 명시해야한다.

```html
{% extends "base.html" %}
```

다음으로는 상속 받는 html의 block에 무엇이 들어갈지 명시해줘야 한다.

이때 block 간의 구분은 block_name으로 한다.

```
{% block style %}
h1 {
    color : red;
}
{% endblock style %}

{% block content %}
<h1>Hello {{ name }}</h1>
{% endblock content %}
```

상속 받은 html의 전체 코드는 아래와 같다.

```
{% extends "base.html" %}

{% block style %}
h1 {
    color : red;
}
{% endblock style %}

{% block content %}
<h1>Hello {{ name }}</h1>
{% endblock content %}
```

## IV. Comments
주석은 다음과 같이 작성한다.

```
{% comment %}
...
{% endcomment %}
```

inline 주석은 다음과 같이 작성한다.

`{# smthing #}`


## V. setting 관련 변수
프로젝트의 settings.py에는 TEMPLATES의 경로를 지정하는 변수가 있다.

아래의 예시 처럼 DIRS에 BASE_DIR의 templates 폴더 내를 추가로 template 경로로 지정할 수 있다.

```python
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR / 'templates',
        ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]
```

