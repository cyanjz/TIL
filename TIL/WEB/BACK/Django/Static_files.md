# Static files
[Django - How to manage static files](https://docs.djangoproject.com/en/4.2/howto/static-files/)
## I. 개요
서버 측에서 변경되지 않고 정적으로 제공되는 파일.

이미지, JS, CSS 파일 등을 포함.

정적 파일을 제공하기 위해서는 html 파일을 특정 url로 연결시킨 것과 마찬가지로 특정 url로 연결해야한다.

핵심은, `URL과 DIR을 settings에 어떻게 정의`하고, `그걸 사용하는 지(DTL, views, models,...)`.

## II. Static files - general

### 1. URL 설정
아래와 같이 pjt의 settings.py에서 url 경로를 지정한다.

기본적으로 `/static/`이 작성되어 있으며, 굳이 변경하지 않는다.

```python
# settings.py
STATIC_URL = '/static/'
```

### 2. 파일 경로 설정
static 파일이 저장될 경로는 기본적으로 `apps/static/`이다.

파일 경로는 아래의 방법으로 추가할 수 있다.
```python
# settings.py
STATICFILES_DIRS = [
    BASE_DIR / 'static'
]
```

### 3. html DTL
static file을 html에서 불러오기 위해서는 static tag를 사용한다.

1. static tag는 built-in DTL tag 가 아니므로 load tag를 사용해서 불러와야한다.
2. static tag의 인자로는 STATIC_DIRS 또는 기본 경로(apps/static)의 경로부터의 상대 경로를 작성한다.

#### img
apps/static 폴더 내의 sample-1.png를 불러오는 dtl.

`{% static 'path_to_static_file' %}`

```html
{% load static %}
<img src="{% static 'articles/sample-1.png' %}">
```

#### link, css
```html
<link rel="stylesheet", href="{% static 'style.css' %}">
```


## III. Media Files
사용자가 업로드한 파일을 관리하고, rendering하는 방법.

Media file은 static file의 일종이다.

### 1. settings.py
`MEDIA_URL`, `MEDIA_ROOT` 작성.

II. static files와 유사하게 `어떤 URL`로 요청했을 때 `어디 있는 파일`을 줄 지 작성하는 것.

```python
# settings.py
MEDIA_URL = 'media/'
MEDIA_ROOT = BASE_DIR / 'media'
```

### 2. project.urls
모든 요청은 결국 urls를 통하므로, project의 urls.py에서 media의 URL로 요청이 들어왔을 때, 응답할 수 있는 기능을 구현.

```python
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    ...
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
```

### 3. Model
받은 이미지를 DB에 저장하고, 나중에 rendering할 때 사용해야 하므로, model에 해당하는 필드를 추가한다.

아래 코드는 이미지를 추가한 model이다. `blank=True`로 설정하여 DB에 빈 값이 들어갈 수 있도록 한다.

참고 : DB에는 실제 이미지 파일이 업로드되는 것이 아니라, image의 경로가 str 형태로 저장된다.

```python
class Article(models.Model):
    title = models.CharField(max_length=10)
    content = models.TextField()
    image = models.ImageField(blank=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
```

### 4. views.py
`form = ArticleForm(request.POST, request.FILES)`

위와 같이 `ModelForm`의 두번째 인자에 `request.FILES`를 전달한다.


### 5. form
html의 form tag에 `enctype="multipart/form-data"` 속성을 추가한다.

[MDN - \<form\>](https://developer.mozilla.org/en-US/docs/Web/HTML/Element/form)

```html
<form active="..." method="POST", enctype="multipart/form-data">
```

### 6. DB 및 저장 확인
- DB에 경로가 저장됨을 확인한다.
- MEDIA_ROOT에 저장된 것을 확인한다.

### 7. media files rendering
아래와 같이 model의 media field의 url 속성에 접근하면 자동으로 `MEDIA_URL`을 사용하여 적절한 url을 반환하게 할 수 있다.

```html
<img src="{{article.image.url}}" alt="img">
```

### 참고 사항
#### 다양한 경로로 media file을 관리하는 방법
media file을 `MEDIA_ROOT`만 지정 가능하고, static file처럼 `STATICFILES_DIRS` 변수를 작성할 수 없다.

media 파일의 세부 경로는 models.py에서 각 field의 `upload_to` 인자를 통해서 조정한다.

```python
# 1. 기본 경로 설정
image = models.ImageField(blank=True, upload_to='images/')

# 2. 업로드 일자를 기준으로 세부 경로 설정
image = models.ImageField(blank=True, upload_to="%Y/%m/%d/")

# 3. 함수 사용
def articles_image_path(instance, filename):
    return f'images/{instance.username}/{filename}'
image = models.ImageField(blank=True, upload_to=articles_image_path(instance, filename))
```

#### 이미지가 계속 쌓이는 현상
- DB에서 이미지를 삭제하거나 수정해도 실제 MEDIA_ROOT에 저장되는 이미지 자체는 변경/삭제가 이뤄지지 않는다.
- django 추가 library를 설치하거나, 외부 서비스에서 보통 처리한다.


#### widget
widget은 form을 사용할 때 tag의 속성들을 지정할 수 있도록 하는 forms.py의 작성 기법이다.

```python
class ArticleForm(forms.ModelForm):

    class Meta:
        model = Article
        fields = '__all__'
        widgets = {
            'title': forms.TextInput(attrs={'class': 'form-control'}),
            'content': forms.Textarea(attrs={'class': 'form-control'}),
            'image_description': forms.Textarea(attrs={'class': 'form-control'}),
            'is_public': forms.CheckboxInput(attrs={'class': 'form-check-input'}),
        }
```