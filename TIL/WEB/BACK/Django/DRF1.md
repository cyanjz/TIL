# DRF
### REST API (Representational State Transfer API)란?

API의 특정한 양식으로 개발 과정에서 앱 사이의 상호작용을 어느정도 규격화된 형태로 수행할 수 있도록 한다.
소프트웨어 설계 방법론의 일종.

자원을 정의하고 자원에 대한 주소를 지정하는 전반적인 방법을 서술.

### Django Rest Framework (DRF)
Django에서 REST API를 다룰 수 있도록 하는 프레임워크.

## I. setup
pip package 설치 후 installed_app에 rest_farmework를 작성한다.
```bash
$pip install djangorestframework
```
```python
# pjt settings.py
INSTALLED_APPS = [
    ...
    'rest_framework',
]
```
 
 <br/>
 <br/>

## II. serializers.py

- ModelSerializer를 상속받아 특정 model에 대해서 직렬화를 수행하는 클래스를 정의.

 ```python
 from rest_framework import serializers
 from .models import Article


 class ArticleListSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = ('id', 'title', 'content', )


class ArticleSerializer(serializers.ModelSerializer):
    class Meta:
        model = Article
        fields = '__all__'
 ```

<br/>
<br/>

## III. urls
이전에는 URL을 나누어서 UPDATE, DELETE등을 별도로 수행했다면, 이제는 하나로 묶어서 처리한다.

(사실 이전에도 view 함수를 하나로 묶을 수는 있었음.)

 ```python
 ...
 # articles.urls.py
 
urlpatterns = [
    path('articles/', views.article_list),
    path('articles/<int:article_pk>/', views.article_detail),
]
 ```

<br/>
<br/>

## IV. views
### i. Custom ModelSerializer
`serializer(model_instance, **kwargs)`
#### args
#### 1. model_instance (READ, CREATE)
ModelSerializer의 첫 위치 인자로 Model instance를 넘겨주면 해당 모델로의 정보를 Serializer에 넘겨줄 수 있다.

해당 값에 model_instance가 내부에 있는 QuerySet이 될 수 있다.

#### 2. data (CREATE, UPDATE)
request.data를 통해 정보를 serializer에 넘겨줄 때 쓰이는 인자.

#### 3. many (READ)
model_instance가 QuerySet 타입일 경우에 True로 설정해야 응답이 적절하게 갈 수 있다.

#### 4. partial (UPDATE)
data에 모든 정보가 있지 않더라도 유효성 검사를 통과해야 할 때 True로 설정한다.

#### methods
#### 1. is_valid()
유효성 검사를 수행하는 serializer의 method.

인자로 `raise_exception=True`를 주면 HTTP 400 응답을 반환.

return : True/False

<br/>


### ii. rest_framework.response.Response
`Response(serializer_info, **kwargs)`
#### 1. serializer_info
serializer.data 또는 serializer.errors를 넘겨준다.

해당 값들이 실질적으로 전달되는 값이다.

#### 2. status
HTTP 응답의 상태코드를 전달하는 키워드 인자.

rest_framework.status의 HTTP 응답을 넣어준다.

`status=status.HTTP_201_CREATED`


 ```python
 from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status

from .models import Article
from .serializers import ArticleListSerializer, ArticleSerializer


# Create your views here.
@api_view(['GET', 'POST'])
def article_list(request):
    if request.method == 'POST':
        # 사용자 입력 데이터를 받아서 클래스로 변환.
        serializer = ArticleSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            # 성공하면 201 CREATED
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        # 실패하면 400 BAD_REQUEST
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    elif request.method == 'GET':
        # 전체 게시글 조회
        articles = Article.objects.all()
        # articles는 django에서만 쓸 수 있는 queryset 데이터.
        # 따라서 serialization을 수행해야 한다.
        serializer = ArticleListSerializer(articles, many=True)
        # DRF에서 제공하는 Response를 사용하여 JSON 데이터를 응답.
        # JSON 데이터는 serializer의 data 속성에 존재함.
        return Response(serializer.data)


# 세부 정보 확인.
@api_view(['GET', 'DELETE', 'PUT'])
def article_detail(request, article_pk):
    article = Article.objects.get(pk=article_pk)
    if request.method == 'GET':
        # 단일 게시글 데이터 조회
        # article serialzier를 통해 직렬화 수행
        serialzer = ArticleSerializer(article)
        return Response(serialzer.data)
    elif request.method == 'DELETE':
        article.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
    elif request.method == 'PUT':
        # 사용자가 보낸 수정 데이터 변환.
        serialzer = ArticleSerializer(article, data=request.data, partial=True)
        if serialzer.is_valid():
            serialzer.save()
            return Response(serialzer.data)
        return Response(serialzer.errors, status=status.HTTP_400_BAD_REQUEST)
 ```


 ## 개념
 