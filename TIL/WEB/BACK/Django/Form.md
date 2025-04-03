# Django Form
사용자로부터 데이터를 수집하고, 처리하기 위한 강력하고 유연한 도구.

사용자의 입력을 처리하기 위해서는 중복, 범위, 보안 등 많은 것을 고려해야한다.

Django form은 이러한 일반적인 고려사항을 사전에 구현하여 데이터를 안전하게 수집하는 강력한 도구이다.

## I. Form class
사용자의 입력 데이터를 수집, 처리 및 유효성 검사를 수행하기 위한 class.

일반적으로 사용자 입력 데이터를 DB에 저장하지 않을 때 쓰인다.

### 1. forms.py에 forms를 상속받은 class 작성.
```python
# articles/forms.py
from django import forms


class ArticleForm(forms.form):
    title = forms.CharField(max_length=10)
    content = forms.CharField()
```

### 2. views.py의 context 수정.
context에 form을 전달한다.

```python
from .forms import ArticleForm


def new(request):
    form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'articles/new.html', context)
```

### 3. template에 form 사용
적절한 label, input tag를 만들어준다.

context에서 사용한 form key를 삽입한다.

```python
{{form}}
```

## II. ModelForm
I. Form class에서 정의한 것과 비슷하게 ModelForm 을 상속 받은 class를 만든다.

선언한 class 내에 Meta class를 선언하여 어떤 모델을 참조할 지 명시한다.

이때, Meta는 python의 inner class 같은 개념으로 어떻게 동작하는 지 생각하는게 아니라, django의 문법으로 받아들여야 한다.

fields를 작성하여 포함할 field를 지정.

```python
# articles/forms.py
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('title', )
```

exclude를 작성하여 제외할 field를 지정.

```python
# articles/forms.py
from .models import Article


class ArticleForm(forms.ModelForm):
    class Meta:
        model = Article
        fields = ('content',)
```


### 1. create
```python
from .forms import ArticleFrom


def create(request):
    if request.method == 'POST':
        form = ArticleForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('articles:index')
    else:
        form = ArticleForm()
    context = {
        'form' : form,
    }
    return render(request, 'create/create.html', context)
```

### 2. update
```python
from .forms import ArticleFrom


def update(request, pk):
    if request.method == 'POST':
        form = ArticleForm(request.POST, instance=Article.objects.get(pk=pk))
        if form.is_valid():
            article = form.save()
            return redirect('articles:detail', article.pk)
    else:
        form = ArticleForm(instance=Article.objects.get(pk=pk))
    context = {
        'form' : form,
    }
    return render(request, 'create/create.html', context)
```

### 3. delete
```python
from .forms import ArticleFrom


def delete(request, pk):
    article = Article.objects.get(pk=pk)
    article.delete()
    return redirect('articles:index')
```


## III. instance methods
### 1. .is_valid()
입력을 views.py의 함수에서 다음과 같은 형식으로 받아올 수 있다.

아래 코드는 사용자의 입력을 받아 유효한 데이터 양식일 경우에는 세부 페이지로 redirect하고,

유효하지 않은 경우에는 해당 form을 전달하여 다시 입력하도록 하는 view 함수의 일부분이다.

이때 html에서 {{form}}과 같은 형태로 input을 rendering 하였다면, form.is_valid()가 False인 경우에는 error message를 포함한 형태로 rendering 한다.
```python
# articles/views.py
form = ArticleForm(request.POST)
if form.is_valid():
    # form.save()는 instance를 반환한다.
    article = form.save()
    return redirect('articles:detail', article.pk)
context = {
    'form' : form,
}
return render(request, 'article/new.html', context)
```

### 2. .save()
save() method는 form을 DB에 저장하고 instance 객체를 반환한다.

form을 특정 객체의 것으로 만드려면, 생성자의 `instance` attribute에 인스턴스를 할당한다.

```python
form = ArticleForm(instance = article)
```

아래와 같이 POST의 data와 instance를 같이 사용할 수 있는데, 이 경우 pk 값만 instacne 변수의 인스턴스, article을 따르고 나머지는 POST의 data를 따른다.

```python
form = ArticleForm(request.POST, instance = article)
```

## IV. forms.field attributes
### 1. label
html에서 rendering 될 label tag의 이름을 지정.

### 2. widget
[Django-widget](https://docs.djangoproject.com/en/5.1/ref/forms/widgets/)

html에서 rendering 될 input의 양식을 지정할 수 있다.

class 변수로 I. forms와 같이 field를 정의하고, 내부 속성을 변경한다.

필드를 정의하고 내부에서 widget을 사용할 때는 forms의 method를 사용한다.

atttr 값은 dict로 준다.
```python
class ArticleForm(forms.ModelForm):
    title = forms.Charfield(
        label='제목',
        widget= forms.TextInput(
            attrs={
                'class' : 'my-title',
                'placeholder' : 'Enter the title',
                'maxlength' : 10,
            }
        )
    )
    content = forms.CharField(
        label='내용',
        widget = forms.TextArea(
            attrs = {
                'class' : 'my-content',
                'placeholder' : 'Enter the content',
                'rows' : 5,
                'cols' : 50,
            }
        )
    )
    class Meta:
        model = Article
        fields = '__all__'
```

```python
from django.forms import ModelForm, Textarea
from myapp.models import Author


class AuthorForm(ModelForm):
    class Meta:
        model = Author
        fields = ["name", "title", "birth_date"]
        widgets = {
            "name": Textarea(attrs={"cols": 80, "rows": 20}),
        }
```

## V. form의 필드를 수동으로 rendering
아래와 같이 form의 속성에 접근하여 직접 rendering할 수도 있다.

`title.non_field_errors` : 필드 값이 없을 때 나오는 error
`form.title.erros` : 해당 field의 error
`form.title.id_for_label` : label의 for에 지정해야 하는 id 값.


```html
{{form.non_field_errors}}
<form action="..." method="POST">
    {% csrf_token %}
    <div>
        {{form.title.errors}}
        <label for="{{form.title.id_for_label}}">Title:</label>
        {{form.title}}
    </div>
    <input type="submit">
</form>
```
